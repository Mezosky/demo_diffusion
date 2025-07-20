"""Magic Transformations tab UI components."""

import gradio as gr
from config.app_config import config
from config.constants import EXAMPLE_MODIFICATIONS, TRANSFORM_TIPS
from .components import (
    create_main_container, create_sidebar_layout, create_content_area,
    create_section_header, create_param_group, create_prompt_section,
    create_slider_with_info, create_primary_button, create_secondary_button,
    create_image_container, create_status_display, create_quick_prompts_section,
    create_tips_section
)


def create_manipulation_tab(model_manager_instance):
    """Creates the 'Magic Transformations' tab UI with sidebar layout."""
    
    with create_main_container():
        # Left Sidebar - Controls
        with create_sidebar_layout():
            create_section_header("Transform Settings", "🪄")
            
            # Transformation Prompt
            param_group, _ = create_param_group("Instructions", "🔮")
            with param_group:
                modification_input = create_prompt_section(
                    "Transformation Instructions",
                    "Transform into Van Gogh painting style...",
                    lines=3
                )
                clear_modify_prompt_btn = create_secondary_button("Clear Instructions")
            
            # Transform Parameters
            param_group, _ = create_param_group("Parameters", "⚙️")
            with param_group:
                guidance_scale_modify = create_slider_with_info(
                    "Text Guidance",
                    minimum=1.0,
                    maximum=20.0,
                    value=config.MANIPULATION_HYPERPARAMS["guidance_scale"],
                    step=0.5,
                    info="How closely to follow transformation instructions"
                )
                
                image_guidance_scale = create_slider_with_info(
                    "Image Preservation",
                    minimum=0.0,
                    maximum=2.0,
                    value=config.MANIPULATION_HYPERPARAMS["image_guidance_scale"],
                    step=0.1,
                    info="How much to preserve original image structure"
                )
                
                num_steps_modify = create_slider_with_info(
                    "Quality Steps",
                    minimum=10,
                    maximum=50,
                    value=config.MANIPULATION_HYPERPARAMS["num_inference_steps"],
                    step=5,
                    info="More steps = higher quality but slower"
                )
                
                seed_modify = gr.Number(
                    label="Seed (-1 for random)",
                    value=config.MANIPULATION_HYPERPARAMS["seed"],
                    precision=0,
                    info="Use same seed for reproducible results"
                )
        
        # Main Content Area
        with create_content_area():
            # Original and Result Images
            with gr.Row():
                with gr.Column():
                    create_section_header("Original Image", "🖼️")
                    input_image_display = create_image_container("", height=400)
                
                with gr.Column():
                    create_section_header("Transformed Result", "✨")
                    modified_image = create_image_container("", height=400)
            
            status_modify = create_status_display("Generate an image first, then transform it!")
            
            # Quick Styles Section - Below images
            create_quick_prompts_section(
                EXAMPLE_MODIFICATIONS, 
                modification_input, 
                title="🎨 Quick Styles"
            )
            
            modify_btn = create_primary_button(
                "🌟 Apply Transform",
                interactive=(model_manager_instance.get_manipulate_pipeline() is not None)
            )
            
            create_tips_section(TRANSFORM_TIPS)

    return (
        input_image_display, modification_input, guidance_scale_modify,
        image_guidance_scale, num_steps_modify, seed_modify, modified_image,
        status_modify, clear_modify_prompt_btn, modify_btn
    )