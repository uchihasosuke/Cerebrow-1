import gradio as gr

from src.webui.webui_manager import WebuiManager
from src.webui.components.agent_settings_tab import create_agent_settings_tab
from src.webui.components.browser_settings_tab import create_browser_settings_tab
from src.webui.components.browser_use_agent_tab import create_browser_use_agent_tab
from src.webui.components.deep_research_agent_tab import create_deep_research_agent_tab
from src.webui.components.load_save_config_tab import create_load_save_config_tab

# Create a custom Glass theme that works with existing settings
custom_glass_theme = gr.themes.Soft().set(
    body_background_fill="linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
    background_fill_primary="rgba(255, 255, 255, 0.15)",
    background_fill_secondary="rgba(255, 255, 255, 0.1)",
    border_color_accent="rgba(255, 255, 255, 0.3)",
    border_color_primary="rgba(255, 255, 255, 0.2)",
    color_accent="rgba(255, 255, 255, 0.95)",
    color_accent_soft="rgba(255, 255, 255, 0.8)",
)

# Add Glass theme to Gradio's available themes
gr.themes.Glass = lambda: custom_glass_theme

theme_map = {
    "Default": gr.themes.Default(),
    "Soft": gr.themes.Soft(),
    "Monochrome": gr.themes.Monochrome(),
    "Glass": custom_glass_theme,
    "Origin": gr.themes.Origin(),
    "Citrus": gr.themes.Citrus(),
    "Ocean": gr.themes.Ocean(),
    "Base": gr.themes.Base()
}


def create_ui(theme_name="Glass"):
    css = """
    .gradio-container {
        width: 70vw !important;
        max-width: 70% !important;
        margin-left: auto !important;
        margin-right: auto !important;
        padding-top: 10px !important;
    }
    
    /* Glass theme specific styles */
    .gradio-container[data-theme="Glass"] {
        background: rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(15px) saturate(120%) !important;
        -webkit-backdrop-filter: blur(15px) saturate(120%) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 16px !important;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1) !important;
    }
    
    .gradio-container[data-theme="Glass"] .main {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        border-radius: 12px !important;
    }
    .header-text {
        text-align: center;
        margin-bottom: 20px;
    }
    .tab-header-text {
        text-align: center;
    }
    .theme-section {
        margin-bottom: 10px;
        padding: 15px;
        border-radius: 10px;
        background: rgba(240, 240, 240, 0.08);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.16);
    }
    /* Hide Gradio's built-in three-dot block menu */
    .gradio-container [data-testid="block-menu"],
    .gradio-container button[aria-label="Options"],
    .gradio-container button[aria-label="Menu"],
    .gradio-container button[aria-label="Open menu"],
    .gradio-container .block-menu,
    .gradio-container .icon-menu {
        display: none !important;
        visibility: hidden !important;
        pointer-events: none !important;
    }
    """

    # remove forced dark mode so Glass theme resembles macOS glass
    js_func = """
    function refresh() { return; }
    """

    ui_manager = WebuiManager()

    with gr.Blocks(
            title="Cerebrow", theme=theme_map[theme_name], css=css, js=js_func,
    ) as demo:
        with gr.Row():
            gr.Markdown(
                """
                # 🧠 Cerebrow
                ### A browser-based AI agent for intelligent web automation
                """,
                elem_classes=["header-text"],
            )
            # Three-dot menu intentionally disabled (hidden from UI)
            # more_menu = gr.Dropdown(
            #     choices=[
            #         "🌐 Browser Settings",
            #         "🎁 Agent Marketplace",
            #         "📁 Load & Save Config",
            #     ],
            #     value=None,
            #     label=None,
            #     show_label=False,
            #     interactive=True,
            #     allow_custom_value=False,
            #     scale=0,
            #     min_width=80,
            # )

        # Hidden content via three-dot menu fully disabled (kept for future reference)
        # with gr.Group(visible=False) as modal_browser_settings:
        #     gr.Markdown("## 🌐 Browser Settings", elem_classes=["tab-header-text"]) 
        #     create_browser_settings_tab(ui_manager)
        #     close_browser_settings_btn = gr.Button("Close", variant="secondary")

        # with gr.Group(visible=False) as modal_marketplace:
        #     gr.Markdown(
        #         """
        #         ## 🎁 Agent Marketplace
        #         ### Agents built on Browser-Use
        #         """,
        #         elem_classes=["tab-header-text"],
        #     )
        #     with gr.Tabs():
        #         with gr.TabItem("Deep Research"):
        #             create_deep_research_agent_tab(ui_manager)
        #     close_marketplace_btn = gr.Button("Close", variant="secondary")

        # with gr.Group(visible=False) as modal_load_save:
        #     gr.Markdown("## 📁 Load & Save Config", elem_classes=["tab-header-text"]) 
        #     create_load_save_config_tab(ui_manager)
        #     close_loadsave_btn = gr.Button("Close", variant="secondary")


        
        # Three-dot menu handlers removed (fully hidden)
        # def on_more_menu(choice: str): ...
        # more_menu.change(...)
        # def close_all(): ...
        # close_browser_settings_btn.click(...)
        # close_marketplace_btn.click(...)
        # close_loadsave_btn.click(...)

        with gr.Tabs() as tabs:
            with gr.TabItem("⚙️ Agent Settings"):
                create_agent_settings_tab(ui_manager)

            # with gr.TabItem("🌐 Browser Settings", visible=False):
            #     create_browser_settings_tab(ui_manager)

            with gr.TabItem("🤖 Run Agent"):
                create_browser_use_agent_tab(ui_manager)

            # with gr.TabItem("🎁 Agent Marketplace", visible=False):
            #     gr.Markdown(
            #         """
            #         ### Agents built on Browser-Use
            #         """,
            #         elem_classes=["tab-header-text"],
            #     )
            #     with gr.Tabs():
            #         with gr.TabItem("Deep Research"):
            #             create_deep_research_agent_tab(ui_manager)

            # with gr.TabItem("📁 Load & Save Config", visible=False):
            #     create_load_save_config_tab(ui_manager)

    return demo
