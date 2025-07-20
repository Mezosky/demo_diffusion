"""CSS styles for the Gradio interface."""

CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap');

* {
    box-sizing: border-box;
}

:root {
    --primary-bg: #0f0f23;
    --secondary-bg: #1a1a2e;
    --card-bg: rgba(26, 26, 46, 0.95);
    --sidebar-bg: rgba(16, 16, 35, 0.98);
    --glass-bg: rgba(255, 255, 255, 0.03);
    --border-color: rgba(255, 255, 255, 0.1);
    --border-light: rgba(255, 255, 255, 0.05);
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    --accent-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    --text-primary: #ffffff;
    --text-secondary: rgba(255, 255, 255, 0.8);
    --text-muted: rgba(255, 255, 255, 0.6);
    --accent-blue: #4facfe;
    --accent-purple: #667eea;
    --accent-pink: #f093fb;
    --success-color: #00f5a0;
    --error-color: #ff6b6b;
    --warning-color: #feca57;
    --shadow-soft: 0 8px 32px rgba(0, 0, 0, 0.3);
    --shadow-strong: 0 16px 64px rgba(0, 0, 0, 0.4);
    --glow-blue: 0 0 30px rgba(79, 172, 254, 0.3);
    --glow-purple: 0 0 30px rgba(102, 126, 234, 0.3);
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: var(--primary-bg);
    color: var(--text-primary);
    margin: 0;
    padding: 0;
    overflow-x: hidden;
    background-image:
        radial-gradient(circle at 25% 25%, rgba(79, 172, 254, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 75% 75%, rgba(102, 126, 234, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 50% 50%, rgba(240, 147, 251, 0.05) 0%, transparent 70%);
    min-height: 100vh;
    line-height: 1.6;
}

.gradio-container {
    max-width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    background: transparent !important;
}

/* Hero Header */
.hero-section {
    text-align: center;
    padding: 1.5rem;
    margin-bottom: 1rem;
    background: var(--card-bg);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border-color);
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow-soft);
}

.hero-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: var(--primary-gradient);
    opacity: 0.1;
    z-index: -1;
}

.hero-title {
    font-size: 2.2rem;
    font-weight: 800;
    margin-bottom: 0.5rem;
    color: #ffffff !important;
    letter-spacing: -0.02em;
    text-shadow: 0 0 20px rgba(79, 172, 254, 0.6);
    filter: drop-shadow(0 0 20px rgba(79, 172, 254, 0.6));
    animation: glow-title 3s ease-in-out infinite alternate;
}

@keyframes glow-title {
    from {
        filter: drop-shadow(0 0 20px rgba(79, 172, 254, 0.6));
    }
    to {
        filter: drop-shadow(0 0 30px rgba(102, 126, 234, 0.8));
    }
}

.hero-subtitle {
    font-size: 1rem;
    color: var(--text-secondary);
    margin: 0;
    font-weight: 400;
}

/* Tab Navigation */
.tab-nav {
    background: var(--card-bg) !important;
    border-radius: 16px !important;
    padding: 8px !important;
    margin-bottom: 1.5rem !important;
    backdrop-filter: blur(20px) !important;
    border: 1px solid var(--border-color) !important;
    box-shadow: var(--shadow-soft) !important;
}

.tab-nav button {
    background: transparent !important;
    color: var(--text-primary) !important;
    border: none !important;
    padding: 12px 24px !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

.tab-nav button.selected {
    background: var(--primary-gradient) !important;
    color: white !important;
    box-shadow: var(--glow-blue) !important;
    transform: translateY(-1px) !important;
}

.tab-nav button:hover:not(.selected) {
    background: var(--glass-bg) !important;
    color: var(--text-primary) !important;
}

/* Images Row - Side by side layout */
.images-row {
    gap: 24px !important;
    margin-bottom: 24px !important;
}

.image-column {
    flex: 1 !important;
    min-width: 0 !important;
}

/* Image Containers */
.image-container {
    border-radius: 16px !important;
    overflow: hidden !important;
    background: rgba(255, 255, 255, 0.95) !important;
    border: 2px solid var(--border-color) !important;
    box-shadow: inset 0 0 20px rgba(0,0,0,0.05), var(--shadow-soft) !important;
    height: 100% !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    min-height: 450px !important;
}

/* Paint component styling */
.image-container .gr-paint {
    background: white !important;
    width: 100% !important;
    height: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
}

.image-container .gr-paint canvas {
    background: white !important;
    border-radius: 12px !important;
    flex-grow: 1;
    width: 100%;
}

.gr-paint > div:has(button):first-child,
.gr-paint > div:has(input[type="color"]):first-child {
    background: var(--sidebar-bg) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 12px !important;
    padding: 8px !important;
    margin-bottom: 8px !important;
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 6px !important;
    justify-content: center !important;
    align-items: center !important;
    flex-shrink: 0;
    order: -1;
}

.gr-paint > div:has(button) button,
.gr-paint > div:has(input[type="color"]) input[type="color"] {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 8px !important;
    color: var(--text-primary) !important;
    padding: 8px 12px !important;
    font-size: 0.85rem !important;
    transition: all 0.3s ease !important;
    cursor: pointer !important;
}

.gr-paint > div:has(button) button:hover {
    background: rgba(255, 255, 255, 0.2) !important;
    border-color: var(--accent-blue) !important;
}

.gr-paint > div:has(button) button.selected,
.gr-paint > div:has(button) button:active {
    background: var(--accent-blue) !important;
    color: white !important;
    border-color: var(--accent-blue) !important;
}

.gr-paint input[type="color"] {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    width: 30px;
    height: 30px;
    background-color: transparent;
    border: 2px solid var(--border-color) !important;
    border-radius: 50% !important;
    cursor: pointer;
    padding: 0;
    margin: 0;
    box-shadow: 0 0 5px rgba(255,255,255,0.2);
}

.gr-paint input[type="color"]::-webkit-color-swatch {
    border-radius: 50%;
    border: 2px solid var(--border-color);
}

.gr-paint input[type="color"]::-webkit-color-swatch-wrapper {
    padding: 0;
}

/* Image display styling */
.image-container img {
    object-fit: contain !important;
    width: 100% !important;
    height: 100% !important;
    border-radius: 12px !important;
}

.image-container canvas {
    object-fit: contain !important;
    width: 100% !important;
    height: 100% !important;
    border-radius: 12px !important;
}

/* Main Layout */
.main-container {
    display: flex;
    height: calc(100vh - 200px);
    gap: 0;
    margin: 0;
    padding: 0;
}

/* Sidebar Styles */
.sidebar-panel {
    width: 320px;
    min-width: 320px;
    max-width: 320px;
    background: var(--sidebar-bg);
    backdrop-filter: blur(25px);
    border-right: 1px solid var(--border-color);
    overflow-y: auto;
    padding: 24px;
    box-shadow: var(--shadow-strong);
}

.sidebar-panel::-webkit-scrollbar {
    width: 6px;
}

.sidebar-panel::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 3px;
}

.sidebar-panel::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.2);
    border-radius: 3px;
}

.sidebar-panel::-webkit-scrollbar-thumb:hover {
    background: rgba(255, 255, 255, 0.3);
}

/* Main Content Area */
.content-area {
    flex: 1;
    display: flex;
    flex-direction: column;
    background: var(--secondary-bg);
    overflow: hidden;
}

.canvas-container {
    flex: 1;
    padding: 24px;
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.result-container {
    height: 300px;
    padding: 24px;
    border-top: 1px solid var(--border-color);
    background: var(--card-bg);
    backdrop-filter: blur(20px);
}

/* Section Headers */
.section-header {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border-light);
}

/* Parameter Groups */
.param-group {
    margin-bottom: 28px;
    padding: 20px;
    background: rgba(255, 255, 255, 0.02);
    border-radius: 12px;
    border: 1px solid var(--border-light);
}

.param-group h4 {
    font-size: 0.9rem;
    font-weight: 600;
    color: var(--accent-blue);
    margin-bottom: 16px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* Input Styling */
input, textarea {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 10px !important;
    color: var(--text-primary) !important;
    padding: 12px 16px !important;
    font-size: 0.9rem !important;
    transition: all 0.3s ease !important;
    backdrop-filter: blur(10px) !important;
    font-family: 'Inter', sans-serif !important;
}

input:focus, textarea:focus {
    border-color: var(--accent-blue) !important;
    box-shadow: 0 0 0 3px rgba(79, 172, 254, 0.15) !important;
    outline: none !important;
    background: rgba(255, 255, 255, 0.08) !important;
}

/* Button Styling */
.btn-primary {
    background: var(--primary-gradient) !important;
    color: white !important;
    border: none !important;
    padding: 14px 28px !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: var(--glow-blue) !important;
    cursor: pointer !important;
    width: 100% !important;
    margin: 20px 0 !important;
}

.btn-primary:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 0 40px rgba(79, 172, 254, 0.4) !important;
}

.btn-secondary {
    background: rgba(255, 255, 255, 0.05) !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border-color) !important;
    padding: 10px 20px !important;
    border-radius: 10px !important;
    font-weight: 500 !important;
    transition: all 0.3s ease !important;
    backdrop-filter: blur(10px) !important;
    width: 100% !important;
    margin-bottom: 12px !important;
}

.btn-secondary:hover {
    background: rgba(255, 255, 255, 0.1) !important;
    transform: translateY(-1px) !important;
}

/* Quick Prompts Section */
.quick-prompts-section {
    background: rgba(255, 255, 255, 0.02) !important;
    border-radius: 12px !important;
    padding: 16px !important;
    border: 1px solid var(--border-light) !important;
    margin-bottom: 16px !important;
}

.quick-prompts-section h4 {
    font-size: 0.9rem !important;
    font-weight: 600 !important;
    color: var(--accent-blue) !important;
    margin-bottom: 12px !important;
    text-align: center !important;
}

.quick-prompts-grid {
    gap: 8px !important;
    justify-content: center !important;
}

.quick-prompt-btn {
    background: rgba(102, 126, 234, 0.1) !important;
    color: var(--accent-purple) !important;
    border: 1px solid rgba(102, 126, 234, 0.2) !important;
    padding: 6px 12px !important;
    border-radius: 6px !important;
    font-size: 0.75rem !important;
    font-weight: 500 !important;
    transition: all 0.3s ease !important;
    backdrop-filter: blur(10px) !important;
    text-align: center !important;
    flex: 1 !important;
    min-width: 0 !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}

.quick-prompt-btn:hover {
    background: rgba(102, 126, 234, 0.2) !important;
    border-color: rgba(102, 126, 234, 0.4) !important;
    transform: translateY(-1px) !important;
}

/* Tips Section */
.tips-minimalistic {
    text-align: center;
    padding: 8px 16px;
    background: rgba(79, 172, 254, 0.05);
    border: 1px solid rgba(79, 172, 254, 0.1);
    border-radius: 8px;
    font-size: 0.8rem;
    color: var(--text-secondary);
    margin-top: 16px;
}

.tips-minimalistic span {
    color: var(--accent-blue);
    font-weight: 600;
}

.tips-section {
    background: rgba(79, 172, 254, 0.1);
    border: 1px solid rgba(79, 172, 254, 0.2);
    border-radius: 12px;
    padding: 16px;
    margin-top: 20px;
}

.tips-section h4 {
    color: var(--accent-blue);
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.tips-section p {
    color: var(--text-secondary);
    font-size: 0.8rem;
    line-height: 1.5;
    margin: 0;
}

/* Prompt Areas */
.prompt-section {
    background: rgba(255, 255, 255, 0.02);
    border-radius: 12px;
    padding: 20px;
    border: 1px solid var(--border-light);
    margin-bottom: 20px;
}

.prompt-section textarea {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 10px !important;
    resize: vertical !important;
    min-height: 80px !important;
}

/* Status Messages */
.status-error {
    background-color: rgba(255, 107, 107, 0.1);
    border: 1px solid var(--error-color);
    color: var(--error-color);
    padding: 10px 15px;
    border-radius: 8px;
    margin: 10px 0;
    text-align: center;
    font-size: 0.9em;
    font-weight: 600;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
}

.status-success {
    background-color: rgba(0, 245, 160, 0.1);
    border: 1px solid var(--success-color);
    color: var(--success-color);
    padding: 10px 15px;
    border-radius: 8px;
    margin: 10px 0;
    text-align: center;
    font-size: 0.9em;
    font-weight: 600;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
}

.status-icon {
    font-size: 1.2em;
    line-height: 1;
}

/* Slider Styling */
.gradio-slider {
    margin: 12px 0 !important;
}

.gradio-slider label {
    font-size: 0.85rem !important;
    font-weight: 500 !important;
    color: var(--text-primary) !important;
    margin-bottom: 8px !important;
    font-family: 'Inter', sans-serif !important;
}

.gradio-slider .info {
    font-size: 0.75rem !important;
    color: var(--text-muted) !important;
    margin-top: 4px !important;
    line-height: 1.4 !important;
}

.gradio-slider input[type="range"] {
    background: rgba(255, 255, 255, 0.08) !important;
    height: 6px !important;
    border-radius: 3px !important;
    outline: none !important;
}

.gradio-slider input[type="range"]::-webkit-slider-thumb {
    background: var(--accent-gradient) !important;
    height: 18px !important;
    width: 18px !important;
    border-radius: 50% !important;
    border: none !important;
    box-shadow: var(--glow-blue) !important;
}

/* Example Buttons */
.example-buttons {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.example-btn {
    background: rgba(102, 126, 234, 0.1) !important;
    color: var(--accent-purple) !important;
    border: 1px solid rgba(102, 126, 234, 0.3) !important;
    padding: 8px 16px !important;
    border-radius: 8px !important;
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    transition: all 0.3s ease !important;
    backdrop-filter: blur(10px) !important;
    text-align: left !important;
    width: 100% !important;
}

.example-btn:hover {
    background: rgba(102, 126, 234, 0.2) !important;
    border-color: rgba(102, 126, 234, 0.5) !important;
    transform: translateY(-1px) !important;
}

/* Progress Indicators */
.progress-container {
    position: relative;
    width: 100%;
    height: 4px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 2px;
    overflow: hidden;
    margin: 16px 0;
}

.progress-bar {
    height: 100%;
    background: var(--accent-gradient);
    border-radius: 2px;
    transition: width 0.3s ease;
    box-shadow: var(--glow-blue);
}

/* Responsive Design */
@media (max-width: 1200px) {
    .main-container {
        flex-direction: column;
        height: auto;
    }
    
    .sidebar-panel {
        width: 100%;
        max-width: none;
        border-right: none;
        border-bottom: 1px solid var(--border-color);
    }
    
    .result-container {
        height: auto;
        min-height: 300px;
    }
}

@media (max-width: 768px) {
    .hero-title {
        font-size: 2rem !important;
    }
    
    .hero-subtitle {
        font-size: 1rem !important;
    }
    
    .sidebar-panel {
        padding: 16px;
    }
    
    .canvas-container {
        padding: 16px;
    }
    
    .param-group {
        padding: 16px;
        margin-bottom: 20px;
    }
}

/* Loading Animation */
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.7; }
}

@keyframes glow {
    0%, 100% { box-shadow: var(--glow-blue); }
    50% { box-shadow: 0 0 40px rgba(79, 172, 254, 0.6); }
}

.loading {
    animation: pulse 2s infinite;
}

.generating {
    animation: glow 2s infinite;
}

/* Custom Gradio Overrides */
.gradio-row {
    gap: 0 !important;
}

.gradio-column {
    padding: 0 !important;
}

.block {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
}

/* Number Input Styling */
input[type="number"] {
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 500 !important;
}

/* Textarea specific */
.gradio-textbox textarea {
    width: 100% !important;
    font-family: 'Inter', sans-serif !important;
}

/* Additional utility classes */
.text-center {
    text-align: center !important;
}

.mt-4 {
    margin-top: 1rem !important;
}

.mb-4 {
    margin-bottom: 1rem !important;
}

.p-4 {
    padding: 1rem !important;
}

/* Focus states for accessibility */
button:focus-visible,
input:focus-visible,
textarea:focus-visible {
    outline: 2px solid var(--accent-blue) !important;
    outline-offset: 2px !important;
}

/* High contrast mode support */
@media (prefers-contrast: high) {
    :root {
        --border-color: rgba(255, 255, 255, 0.3);
        --text-secondary: rgba(255, 255, 255, 0.9);
    }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}
"""