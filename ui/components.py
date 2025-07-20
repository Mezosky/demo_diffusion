"""UI components for the Gradio interface."""

import gradio as gr
from config.constants import EXAMPLE_PROMPTS, EXAMPLE_MODIFICATIONS


def create_hero_section():
    """Create the hero header section."""
    return gr.HTML("""
    <div class="hero-section">
        <h1 class="hero-title">🎨 SketchMagic Studio ✨</h1>
        <p class="hero-subtitle">Transform your sketches into stunning AI-generated artwork</p>
    </div>
    """)


def create_section_header(title, icon=""):
    """Create a styled section header."""
    return gr.HTML(f'<div class="section-header">{icon} {title}</div>')


def create_param_group(title, icon=""):
    """Create a parameter group container."""
    return gr.Group(elem_classes=["param-group"]), gr.HTML(f'<h4>{icon} {title}</h4>')


def create_quick_prompts_section(prompts, output_component, title="💡 Quick Prompts"):
    """Create a section with quick prompt buttons."""
    with gr.Group(elem_classes=["quick-prompts-section"]):
        gr.HTML(f'<h4>{title}</h4>')
        
        # Split prompts into rows of 3
        mid_point = len(prompts) // 2
        
        with gr.Row(elem_classes=["quick-prompts-grid"]):
            for prompt in prompts[:mid_point]:
                btn_text = prompt.split(',')[0]
                if len(btn_text) > 20:
                    btn_text = btn_text[:20] + "..."
                btn = gr.Button(btn_text, elem_classes=["quick-prompt-btn"])
                btn.click(lambda text=prompt: text, outputs=output_component)
        
        with gr.Row(elem_classes=["quick-prompts-grid"]):
            for prompt in prompts[mid_point:]:
                btn_text = prompt.split(',')[0]
                if len(btn_text) > 20:
                    btn_text = btn_text[:20] + "..."
                btn = gr.Button(btn_text, elem_classes=["quick-prompt-btn"])
                btn.click(lambda text=prompt: text, outputs=output_component)


def create_tips_section(tips_text):
    """Create a minimalistic tips section."""
    return gr.HTML(f"""
    <div class="tips-minimalistic" style="margin-top: -15px;">
        {tips_text}
    </div>
    """)


def create_prompt_section(label, placeholder, lines=3):
    """Create a styled prompt input section."""
    return gr.Textbox(
        label=label,
        placeholder=placeholder,
        lines=lines,
        elem_classes=["prompt-section"]
    )


def create_slider_with_info(label, minimum, maximum, value, step, info=None):
    """Create a styled slider with optional info text."""
    return gr.Slider(
        minimum=minimum,
        maximum=maximum,
        value=value,
        step=step,
        label=label,
        info=info
    )


def create_primary_button(label, interactive=True):
    """Create a primary action button."""
    return gr.Button(
        label,
        elem_classes=["btn-primary"],
        interactive=interactive
    )


def create_secondary_button(label):
    """Create a secondary action button."""
    return gr.Button(
        label,
        elem_classes=["btn-secondary"]
    )


def create_image_container(label, height=450, interactive=False, image_type="pil"):
    """Create a styled image container."""
    return gr.Image(
        label=label,
        height=height,
        width="100%",
        interactive=interactive,
        type=image_type,
        elem_classes=["image-container"]
    )


def create_paint_canvas(height=450):
    """Create a styled paint canvas."""
    return gr.Paint(
        label="",
        height=height,
        width="100%",
        type="pil",
        elem_classes=["image-container"]
    )


def create_sidebar_layout():
    """Create the sidebar column layout."""
    return gr.Column(elem_classes=["sidebar-panel"])


def create_content_area():
    """Create the main content area layout."""
    return gr.Column(elem_classes=["content-area"])


def create_main_container():
    """Create the main container layout."""
    return gr.Row(elem_classes=["main-container"])


def create_images_row():
    """Create the images row layout."""
    return gr.Row(elem_classes=["images-row"])


def create_image_column():
    """Create an image column layout."""
    return gr.Column(elem_classes=["image-column"])


def create_status_display(initial_message):
    """Create a status display component."""
    return gr.HTML(value=f"<p style='text-align:center; color: var(--text-muted);'>{initial_message}</p>")


def setup_example_buttons(examples, target_component):
    """Setup example buttons that populate a target component."""
    buttons = []
    for example in examples:
        btn_text = example.split(',')[0]
        if len(btn_text) > 25:
            btn_text = btn_text[:25] + "..."
        
        btn = gr.Button(btn_text, elem_classes=["quick-prompt-btn"])
        btn.click(lambda text=example: text, outputs=target_component)
        buttons.append(btn)
    
    return buttons