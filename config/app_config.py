"""Application configuration and hyperparameters."""

import torch


class AppConfig:
    """Central configuration class for the application."""
    
    # Device and Data Type Configuration
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    DTYPE = torch.float32
    
    def __init__(self):
        self._configure_device_and_dtype()
    
    def _configure_device_and_dtype(self):
        """Configure device and data type based on available hardware."""
        if self.DEVICE == "cuda":
            # Check for CUDA
            if torch.cuda.get_device_properties(0).major >= 8:
                self.DTYPE = torch.float16
                print("Using torch.float16 for CUDA (Ampere or newer GPU).")
            else:
                self.DTYPE = torch.float16
                print("Using torch.float16 for CUDA (older GPU, consider compatibility).")
        else:
            print("Using torch.float32 for CPU.")

    # Model IDs
    CONTROLNET_MODEL_ID = "lllyasviel/sd-controlnet-scribble"
    STABLE_DIFFUSION_MODEL_ID = "runwayml/stable-diffusion-v1-5"
    INSTRUCTPIX2PIX_MODEL_ID = "timbrooks/instruct-pix2pix"

    # Default Hyperparameters for Sketch to Image (First Tab)
    SKETCH_HYPERPARAMS = {
        "guidance_scale": 7.5,
        "num_inference_steps": 20,
        "controlnet_conditioning_scale": 1.0,
        "seed": -1,  # -1 for random
    }

    # Default Hyperparameters for Image Manipulation (Second Tab)
    MANIPULATION_HYPERPARAMS = {
        "guidance_scale": 7.5,
        "image_guidance_scale": 1.5,
        "num_inference_steps": 20,
        "seed": -1,
    }

config = AppConfig()