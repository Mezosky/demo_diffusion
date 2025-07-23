# ✨ Demo Diffusion

<p align="center">
  <img src="./resources/how-to-use-record.gif" alt="SketchMagic Studio Demo" width="500"/>
</p>

A modular, production-ready **Gradio application** for AI-powered **sketch-to-image generation** and **artistic image transformation**, built on **Stable Diffusion** and **ControlNet**.

## 🚀 Features

- **Sketch to Image**: Transform hand-drawn sketches into high-quality images using ControlNet
- **Magic Transformations**: Apply artistic styles and modifications to generated images using InstructPix2Pix
- **Modular Architecture**: Maintainable code structure
- **GPU Optimization**: Automatic VRAM detection and memory management
- **Quick Prompts**: Pre-built example prompts and styles for rapid experimentation

## 📁 Project Structure

```
demo-diffusion/
├── app.py                    # Main application entry point
├── config/
│   ├── __init__.py
│   ├── app_config.py        # Configuration and hyperparameters
│   └── constants.py         # Constants and example data
├── models/
│   ├── __init__.py
│   └── model_manager.py     # Model loading and management
├── core/
│   ├── __init__.py
│   ├── image_processing.py  # Image preprocessing functions
│   └── generation.py       # Core generation logic
├── ui/
│   ├── __init__.py
│   ├── styles.py           # CSS styles
│   ├── components.py       # Reusable UI components
│   ├── sketch_tab.py       # Sketch to image tab
│   └── transform_tab.py    # Magic transformations tab
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- CUDA-compatible GPU (recommended, 6GB+ VRAM)
- Git

### Setup Steps

1. **Clone the repository:**
```bash
git clone https://github.com/Mezosky/demo_diffusion.git
cd demo_diffusion
```

2. **Install dependencies:**
```bash
conda env create -f environment.yml
```

3. **Run the app!!**
```bash
conda activate aiartistic
python app.py
```


### Environment Variables

Set these environment variables to customize behavior:

```bash
export CUDA_VISIBLE_DEVICES=0  # Select specific GPU
export TORCH_HOME=/path/to/models  # Custom model cache directory
```

## 🎯 Usage Guide

### Sketch to Image

1. Draw a sketch on the canvas using the drawing tools
2. Enter a detailed text prompt describing your vision
3. Adjust generation parameters:
   - **Guidance Scale**: How closely to follow the prompt (7.5 recommended)
   - **Sketch Influence**: How much the sketch controls output (1.0 recommended)
   - **Quality Steps**: More steps = higher quality but slower (20 recommended)
   - **Seed**: Set for reproducible results (-1 for random)
4. Click "🚀 Generate Image"

### Magic Transformations

1. First generate an image in the Sketch to Image tab
2. Enter transformation instructions (e.g., "Transform into Van Gogh style")
3. Adjust transformation parameters:
   - **Text Guidance**: How closely to follow instructions (7.5 recommended)
   - **Image Preservation**: How much to preserve original structure (1.5 recommended)
   - **Quality Steps**: Processing steps (20 recommended)
4. Click "🌟 Apply Transform"

## ⚙️ Configuration

### Model Configuration

Edit `config/app_config.py` to change model settings:

```python
class AppConfig:
    # Model IDs
    CONTROLNET_MODEL_ID = "lllyasviel/sd-controlnet-scribble"
    STABLE_DIFFUSION_MODEL_ID = "runwayml/stable-diffusion-v1-5"
    INSTRUCTPIX2PIX_MODEL_ID = "timbrooks/instruct-pix2pix"
    
    # Default parameters
    SKETCH_HYPERPARAMS = {
        "guidance_scale": 7.5,
        "num_inference_steps": 20,
        "controlnet_conditioning_scale": 1.0,
        "seed": -1,
    }
```

---

**Happy Sketching! 🎨✨**