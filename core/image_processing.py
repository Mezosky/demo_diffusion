"""Image preprocessing and utility functions."""

from PIL import Image
import numpy as np


def preprocess_sketch_input(sketch_image):
    """
    Ensures the sketch input is a PIL Image and converts it for ControlNet.
    
    Args:
        sketch_image: Input from Gradio Paint component
        
    Returns:
        tuple: (processed_image, error_message)
    """
    if sketch_image is None:
        return None, "Please draw something on the canvas!"

    if isinstance(sketch_image, dict):
        # Gradio 4.0 returns dict for Paint if clear is used
        if 'image' in sketch_image and sketch_image['image'] is not None:
            sketch_image = sketch_image['image']
        elif 'composite' in sketch_image and sketch_image['composite'] is not None:
            sketch_image = sketch_image['composite']
        else:
            return None, "Invalid image format received from sketch input. Please draw again or clear."
    
    if not isinstance(sketch_image, Image.Image):
        if isinstance(sketch_image, np.ndarray):
            sketch_image = Image.fromarray(sketch_image)
        else:
            return None, "Invalid image format received from sketch input. Please draw again."

    sketch_image = sketch_image.convert("L").convert("RGB")
    return sketch_image, None


def ensure_rgb_format(image):
    """
    Ensure image is in RGB format.
    
    Args:
        image: PIL Image
        
    Returns:
        PIL Image in RGB format
    """
    if image.mode != "RGB":
        return image.convert("RGB")
    return image


def validate_image_input(image, error_message_prefix="Image"):
    """
    Validate that an image input is valid.
    
    Args:
        image: Image to validate
        error_message_prefix: Prefix for error messages
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if image is None:
        return False, f"{error_message_prefix} is required!"
    
    if not isinstance(image, Image.Image):
        return False, f"Invalid {error_message_prefix.lower()} format!"
    
    return True, None