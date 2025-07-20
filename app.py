import gradio as gr

# Import configuration and models
from config.app_config import config
from models.model_manager import ModelManager

# Import core functionality
from core.generation import ImageGenerator

# Import UI components
from ui.styles import CUSTOM_CSS
from ui.components import create_hero_section
from ui.sketch_tab import create_sketch_tab
from ui.transform_tab import create_manipulation_tab


class SketchMagicApp:
    """Main application class for SketchMagic Studio."""
    
    def __init__(self):
        self.model_manager = None
        self.image_generator = None
        self.demo = None
        self._initialize_models()
        self._create_interface()
    
    def _initialize_models(self):
        """Initialize the model manager and image generator."""
        print("🎨 Initializing Sketch to Magic...")
        self.model_manager = ModelManager()
        self.image_generator = ImageGenerator(self.model_manager)
    
    def _create_interface(self):
        """Create the main Gradio interface."""
        with gr.Blocks(
            css=CUSTOM_CSS, 
            title="🎨 SketchMagic Studio ✨", 
            theme=gr.themes.Soft()
        ) as self.demo:
            # Hero Header
            create_hero_section()

            # System Status
            initial_status = self.model_manager.get_load_status()
            gr.HTML(initial_status)

            # Shared state for images
            generated_image_placeholder = gr.State(None)

            # Tabs
            with gr.Tabs(elem_classes=["tab-nav"]):
                with gr.Tab("🖊️ Sketch to Image", elem_id="sketch-tab"):
                    sketch_components = create_sketch_tab(self.model_manager)
                
                with gr.Tab("🔮 Magic Transformations", elem_id="modify-tab"):
                    transform_components = create_manipulation_tab(self.model_manager)

            # Setup event handlers
            self._setup_event_handlers(sketch_components, transform_components, generated_image_placeholder)
    
    def _setup_event_handlers(self, sketch_components, transform_components, generated_image_placeholder):
        """Setup all event handlers for the interface."""
        # Unpack components
        (sketch_input, prompt_input, negative_prompt_input, guidance_scale_sketch, 
         num_steps_sketch, seed_sketch, controlnet_scale, generated_image_output_sketch, 
         status_sketch, clear_prompts_btn, generate_btn) = sketch_components
        
        (input_image_display_manipulation, modification_input,
         guidance_scale_modify, image_guidance_scale, num_steps_modify, seed_modify,
         modified_image_output_manipulation, status_modify,
         clear_modify_prompt_btn, modify_btn) = transform_components

        # Clear buttons
        clear_prompts_btn.click(
            fn=lambda: ("", ""),
            outputs=[prompt_input, negative_prompt_input]
        )
        
        clear_modify_prompt_btn.click(lambda: "", outputs=modification_input)

        # Generate image from sketch
        generate_btn.click(
            fn=self.image_generator.generate_from_sketch,
            inputs=[
                sketch_input, prompt_input, negative_prompt_input,
                guidance_scale_sketch, num_steps_sketch, seed_sketch, controlnet_scale
            ],
            outputs=[generated_image_output_sketch, status_sketch],
            show_progress="full"
        ).then(
            fn=lambda img: img,
            inputs=[generated_image_output_sketch],
            outputs=[generated_image_placeholder]
        ).then(
            fn=lambda img_state: img_state,
            inputs=[generated_image_placeholder],
            outputs=[input_image_display_manipulation]
        )

        # Transform image
        modify_btn.click(
            fn=self.image_generator.transform_image,
            inputs=[
                generated_image_placeholder, modification_input,
                guidance_scale_modify, image_guidance_scale, num_steps_modify, seed_modify
            ],
            outputs=[modified_image_output_manipulation, status_modify],
            show_progress="full"
        )
    
    def launch(self, share=False, inbrowser=True, server_name="0.0.0.0", server_port=None):
        """Launch the Gradio application."""
        if self.demo is None:
            raise RuntimeError("Interface not created. Call _create_interface() first.")
        
        self.demo.launch(
            share=share,
            inbrowser=inbrowser,
            show_error=True,
            server_name=server_name,
            server_port=server_port
        )


def main():
    """Main entry point for the application."""
    app = SketchMagicApp()
    app.launch()


if __name__ == "__main__":
    main()