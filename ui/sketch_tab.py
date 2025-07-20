"""Sketch to Image tab UI components."""

import gradio as gr
from config.app_config import config
from config.constants import EXAMPLE_PROMPTS, DRAWING_TIPS
from .components import (
    create_main_container, create_sidebar_layout, create_content_area,
    create_section_header, create_param_group, create_prompt_section,
    create_slider_with_info, create_primary_button, create_secondary_button,
    create_images_row, create_image_column, create_paint_canvas,
    create_image_container, create_status_display, create_quick_prompts_section,
    create_tips_section
)


def create_sketch_tab(model_manager_instance):
    """Creates the 'Sketch to Image' tab UI with sidebar layout."""
    
    with create_main_container():
        # Left Sidebar - Controls
        with create_sidebar_layout():
            create_section_header("Generation Settings", "⚙️")
            
            # Prompt Section
            param_group, _ = create_param_group("Prompt", "📝")
            with param_group:
                prompt_input = create_prompt_section(
                    "Describe Your Vision",
                    "A majestic lion in golden savanna, photorealistic...",
                    lines=3
                )
                
                negative_prompt_input = create_prompt_section(
                    "Negative Prompt",
                    "blurry, low quality, distorted...",
                    lines=2
                )
                
                clear_prompts_btn = create_secondary_button("Clear Prompts")
            
            # Generation Parameters
            param_group, _ = create_param_group("Parameters", "🎯")
            with param_group:
                guidance_scale_sketch = create_slider_with_info(
                    "Guidance Scale",
                    minimum=1.0,
                    maximum=20.0,
                    value=config.SKETCH_HYPERPARAMS["guidance_scale"],
                    step=0.5,
                )
                
                controlnet_scale = create_slider_with_info(
                    "Sketch Influence",
                    minimum=0.0,
                    maximum=1.5,
                    value=config.SKETCH_HYPERPARAMS["controlnet_conditioning_scale"],
                    step=0.05,
                )
                
                num_steps_sketch = create_slider_with_info(
                    "Quality Steps",
                    minimum=10,
                    maximum=50,
                    value=config.SKETCH_HYPERPARAMS["num_inference_steps"],
                    step=5,
                )
                
                seed_sketch = gr.Number(
                    label="Seed (-1 for random)",
                    value=config.SKETCH_HYPERPARAMS["seed"],
                    precision=0,
                )
        
        # Main Content Area - Side by side images
        with create_content_area():
            # Canvas and Result Side by Side
            with create_images_row():
                # Canvas Section
                with create_image_column():
                    create_section_header("Drawing Canvas", "✏️")
                    sketch_input = create_paint_canvas(height=450)
                
                # Result Section
                with create_image_column():
                    create_section_header("Generated Result", "🖼️")
                    generated_image = create_image_container("", height=450)
                    status_sketch = create_status_display("Draw and generate your vision!")
            
            # Quick Examples Section - Below images
            create_quick_prompts_section(EXAMPLE_PROMPTS, prompt_input)
            
            generate_btn = create_primary_button(
                "🚀 Generate Image",
                interactive=(model_manager_instance.get_sketch_pipeline() is not None)
            )
            
            # Drawing Tips - Minimalistic
            create_tips_section(DRAWING_TIPS)

    return (
        sketch_input, prompt_input, negative_prompt_input, guidance_scale_sketch,
        num_steps_sketch, seed_sketch, controlnet_scale, generated_image,
        status_sketch, clear_prompts_btn, generate_btn
    )