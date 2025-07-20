"""Model management and loading functionality."""

import torch
import gc
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel, UniPCMultistepScheduler
from diffusers import StableDiffusionInstructPix2PixPipeline

from config.app_config import config


class ModelManager:
    """Singleton class for managing AI models."""
    
    _instance = None
    _pipe_sketch = None
    _pipe_manipulate = None
    _initial_load_error = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelManager, cls).__new__(cls)
            cls._instance._load_models_internal()
        return cls._instance

    def _load_models_internal(self):
        """Internal method to load and cache the models."""
        if self._pipe_sketch is not None and self._pipe_manipulate is not None:
            print("✅ Models already loaded.")
            return

        print(f"🚀 Attempting to load AI models to {config.DEVICE} with {config.DTYPE} precision...")

        current_device_candidate = config.DEVICE
        current_dtype_candidate = config.DTYPE
        temp_error_message = None

        try:
            if current_device_candidate == "cuda":
                total_memory_bytes = torch.cuda.get_device_properties(0).total_memory
                total_memory_gb = total_memory_bytes / (1024**3)
                print(f"CUDA device has {total_memory_gb:.2f} GB VRAM.")

                if total_memory_gb < 6:
                    temp_error_message = f"❌ Insufficient VRAM detected ({total_memory_gb:.2f} GB). At least 6-8 GB recommended for these models on GPU. Attempting to switch to CPU, which will be very slow."
                    print(temp_error_message)
                    current_device_candidate = "cpu"
                    current_dtype_candidate = torch.float32
                elif total_memory_gb < 10 and current_dtype_candidate == torch.float32:
                    print("⚠️ Warning: Less than 10GB VRAM detected. Consider using float16 for better memory efficiency (if not already) and ensure `xformers` is installed for optimal performance.")

            if current_device_candidate == "cpu":
                print("Running on CPU. Model loading and inference will be significantly slower.")
                current_dtype_candidate = torch.float32

            self._load_sketch_model(current_device_candidate, current_dtype_candidate)
            self._load_manipulation_model(current_device_candidate, current_dtype_candidate)
            self._move_models_to_device(current_device_candidate)
            self._enable_optimizations(current_device_candidate)

            print("✅ Models loaded successfully!")
            self._initial_load_error = None

        except Exception as e:
            self._handle_loading_error(e, current_device_candidate)

    def _load_sketch_model(self, device, dtype):
        """Load the sketch-to-image model."""
        print(f"Loading ControlNet model: {config.CONTROLNET_MODEL_ID}")
        controlnet = ControlNetModel.from_pretrained(
            config.CONTROLNET_MODEL_ID,
            torch_dtype=dtype,
            local_files_only=False
        )

        print(f"Loading Stable Diffusion Pipeline: {config.STABLE_DIFFUSION_MODEL_ID}")
        self._pipe_sketch = StableDiffusionControlNetPipeline.from_pretrained(
            config.STABLE_DIFFUSION_MODEL_ID,
            controlnet=controlnet,
            torch_dtype=dtype,
            local_files_only=False
        )
        self._pipe_sketch.scheduler = UniPCMultistepScheduler.from_config(
            self._pipe_sketch.scheduler.config
        )

    def _load_manipulation_model(self, device, dtype):
        """Load the image manipulation model."""
        print(f"Loading InstructPix2Pix Pipeline: {config.INSTRUCTPIX2PIX_MODEL_ID}")
        self._pipe_manipulate = StableDiffusionInstructPix2PixPipeline.from_pretrained(
            config.INSTRUCTPIX2PIX_MODEL_ID,
            torch_dtype=dtype,
            safety_checker=None,
            local_files_only=False
        )

    def _move_models_to_device(self, device):
        """Move models to the specified device."""
        print(f"Moving models to {device}...")
        self._pipe_sketch.to(device)
        self._pipe_manipulate.to(device)

    def _enable_optimizations(self, device):
        """Enable performance optimizations if available."""
        if device == "cuda":
            try:
                import xformers
                self._pipe_sketch.enable_xformers_memory_efficient_attention()
                self._pipe_manipulate.enable_xformers_memory_efficient_attention()
                print("XFormers attention enabled for performance.")
            except ImportError:
                print("XFormers not found. Install 'xformers' for optimal CUDA performance (`pip install xformers`).")
            except Exception as e:
                print(f"Warning: Could not enable xformers memory attention: {e}")

    def _handle_loading_error(self, error, device):
        """Handle and categorize loading errors."""
        detailed_error = f"❌ Error during model loading: {error}"
        print(detailed_error)
        
        error_str = str(error).lower()
        
        if any(keyword in error_str for keyword in ["cuda out of memory", "hiplaunchkernel", "out of memory"]):
            self._initial_load_error = "❌ GPU Memory (VRAM) Error: Insufficient VRAM to load models. Try a GPU with more memory or ensure `xformers` is installed and `diffusers` is updated. Attempting to fall back to CPU."
            if device == "cuda":
                print("Attempting to retry on CPU due to VRAM error...")
                self._cleanup_models()
                config.DEVICE = "cpu"
                config.DTYPE = torch.float32
                self._load_models_internal()
        elif any(keyword in error_str for keyword in ["cannot load", "safetensors_rust", "filenotfounderror"]):
            self._initial_load_error = f"❌ Model File Error: Could not load model files. Check internet connection, disk space, or try clearing Hugging Face cache. Error: {error}"
        elif "enable_xformers_memory_efficient_attention" in error_str:
            self._initial_load_error = f"❌ Compatibility Error: Your 'diffusers' library version might be too old or incompatible with `xformers`. Please run `pip install --upgrade diffusers transformers accelerate` and `pip install xformers`."
        else:
            self._initial_load_error = f"❌ An unexpected error occurred during model loading. Check console for details. Error: {error}"

        self._cleanup_models()

    def _cleanup_models(self):
        """Cleans up loaded models and clears GPU cache."""
        if self._pipe_sketch:
            del self._pipe_sketch
            self._pipe_sketch = None
        if self._pipe_manipulate:
            del self._pipe_manipulate
            self._pipe_manipulate = None
        if config.DEVICE == "cuda":
            torch.cuda.empty_cache()
        gc.collect()

    def get_sketch_pipeline(self):
        """Get the sketch-to-image pipeline."""
        return self._pipe_sketch

    def get_manipulate_pipeline(self):
        """Get the image manipulation pipeline."""
        return self._pipe_manipulate

    def get_load_status(self):
        """Get the current loading status as HTML."""
        if self._initial_load_error:
            return f'<div class="status-error">{self._initial_load_error}</div>'
        else:
            return f'<div class="status-success"><span class="status-icon">✅</span><strong>AI Models Ready!</strong> Running on <strong>{config.DEVICE.upper()}</strong></div>'

    def cleanup_memory(self):
        """Clean up GPU memory after generation."""
        if config.DEVICE == "cuda":
            torch.cuda.empty_cache()
            gc.collect()