"""Core image generation and transformation logic."""

import torch
import gradio as gr

from config.app_config import config
from .image_processing import preprocess_sketch_input, ensure_rgb_format, validate_image_input


class ImageGenerator:
    """Handles image generation and transformation operations."""
    
    def __init__(self, model_manager):
        self.model_manager = model_manager
    
    def generate_from_sketch(self, sketch_input_data, prompt, negative_prompt, 
                           guidance_scale, num_inference_steps, seed, 
                           controlnet_conditioning_scale, progress=gr.Progress()):
        """
        Converts a user sketch into a generated image based on a text prompt.
        
        Args:
            sketch_input_data: Input from Gradio Paint component
            prompt: Text description of desired image
            negative_prompt: What to avoid in the image
            guidance_scale: How closely to follow the prompt
            num_inference_steps: Number of denoising steps
            seed: Random seed (-1 for random)
            controlnet_conditioning_scale: How much to follow the sketch
            progress: Gradio progress tracker
            
        Returns:
            tuple: (generated_image, status_html)
        """
        pipe_sketch = self.model_manager.get_sketch_pipeline()
        if pipe_sketch is None:
            return None, f'<div class="status-error">❌ Sketch-to-Image model not loaded. {self.model_manager.get_load_status()}</div>'

        # Preprocess sketch input
        sketch_image, error_message = preprocess_sketch_input(sketch_input_data)
        if error_message:
            return None, f'<div class="status-error">❌ {error_message}</div>'

        # Validate prompt
        if not prompt or prompt.strip() == "":
            return None, '<div class="status-error">❌ Please provide a detailed description of your sketch!</div>'

        try:
            progress(0.1, desc="🎨 Preparing your sketch...")

            # Setup generator for reproducible results
            generator = None
            if seed != -1:
                generator = torch.Generator(config.DEVICE).manual_seed(int(seed))

            conditioning_scale = float(controlnet_conditioning_scale)

            # Generate image
            with torch.autocast(config.DEVICE):
                result = pipe_sketch(
                    prompt=prompt,
                    negative_prompt=negative_prompt if negative_prompt and negative_prompt.strip() else None,
                    image=sketch_image,
                    num_inference_steps=int(num_inference_steps),
                    guidance_scale=float(guidance_scale),
                    controlnet_conditioning_scale=conditioning_scale,
                    generator=generator
                )

            generated_img = result.images[0]

            # Cleanup memory
            del result
            self.model_manager.cleanup_memory()

            progress(1.0, desc="✨ Masterpiece created!")
            return generated_img, '<div class="status-success"><span class="status-icon">🎉</span>Success! Your sketch has been transformed!</div>'

        except Exception as e:
            return self._handle_generation_error(e, "generating")

    def transform_image(self, generated_image, manipulation_prompt, guidance_scale, 
                       image_guidance_scale, num_inference_steps, seed, 
                       progress=gr.Progress()):
        """
        Manipulates an existing image based on a text instruction.
        
        Args:
            generated_image: Source image to transform
            manipulation_prompt: Text instruction for transformation
            guidance_scale: How closely to follow the text prompt
            image_guidance_scale: How much to preserve original image
            num_inference_steps: Number of denoising steps
            seed: Random seed (-1 for random)
            progress: Gradio progress tracker
            
        Returns:
            tuple: (modified_image, status_html)
        """
        pipe_manipulate = self.model_manager.get_manipulate_pipeline()
        if pipe_manipulate is None:
            return None, f'<div class="status-error">❌ Image Manipulation model not loaded. {self.model_manager.get_load_status()}</div>'

        # Validate inputs
        is_valid, error_msg = validate_image_input(generated_image, "Generated image")
        if not is_valid:
            return None, f'<div class="status-error">❌ Please generate an image first in the \'Sketch to Image\' tab!</div>'

        if not manipulation_prompt or manipulation_prompt.strip() == "":
            return None, '<div class="status-error">❌ Please describe how you want to modify the image!</div>'

        try:
            progress(0.2, desc="🔮 Reading your instructions...")

            # Setup generator for reproducible results
            generator = None
            if seed != -1:
                generator = torch.Generator(config.DEVICE).manual_seed(int(seed))

            # Ensure image is in RGB format
            generated_image = ensure_rgb_format(generated_image)

            progress(0.5, desc="✨ Applying magical transformations...")

            # Transform image
            with torch.autocast(config.DEVICE):
                result = pipe_manipulate(
                    prompt=manipulation_prompt,
                    image=generated_image,
                    guidance_scale=float(guidance_scale),
                    num_inference_steps=int(num_inference_steps),
                    image_guidance_scale=float(image_guidance_scale),
                    generator=generator
                )

            modified_img = result.images[0]

            # Cleanup memory
            del result
            self.model_manager.cleanup_memory()

            progress(1.0, desc="🪄 Transformation complete!")
            return modified_img, '<div class="status-success"><span class="status-icon">✨</span>Amazing! Your image has been transformed!</div>'

        except Exception as e:
            return self._handle_generation_error(e, "manipulation")

    def _handle_generation_error(self, error, operation_type):
        """
        Handle errors during generation or transformation.
        
        Args:
            error: The exception that occurred
            operation_type: Type of operation ("generating" or "manipulation")
            
        Returns:
            tuple: (None, error_html)
        """
        error_msg = f"❌ Error during {operation_type}: {str(error)}"
        print(f"Error in {operation_type}: {error}")
        
        error_str = str(error).lower()
        if any(keyword in error_str for keyword in ["cuda out of memory", "hiplaunchkernel", "out of memory"]):
            error_msg = f"❌ GPU Memory (VRAM) Error during {operation_type}. Try reducing image size or complexity, or free up GPU memory. If the issue persists, restart the app."
        
        return None, f'<div class="status-error">{error_msg}</div>'