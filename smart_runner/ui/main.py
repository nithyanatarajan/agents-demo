import asyncio

import gradio as gr

from smart_runner.config import MODELS, PROVIDERS
from smart_runner.ui.browser_agent import run_browser_task


def update_models_for(provider):
    """Updates model choices based on selected provider."""
    return gr.Dropdown(choices=MODELS[provider], value=MODELS[provider][0])


def toggle_button(task):
    """Enable the button only if task is not empty."""
    return gr.Button(interactive=bool(task.strip()))


def create_ui():
    with gr.Blocks(title='Browser Use GUI') as interface:
        gr.Markdown('# Browser Use Task Automation')

        with gr.Row():
            with gr.Column():
                task = gr.Textbox(
                    label='Task Description',
                    placeholder='E.g., Find flights from New York to London '
                    'for next week',
                    lines=3,
                )
                provider = gr.Dropdown(
                    choices=PROVIDERS,
                    label='Provider',
                    value=PROVIDERS[0],
                )
                model = gr.Dropdown(
                    choices=MODELS[PROVIDERS[0]],
                    label='Model',
                    value=MODELS[PROVIDERS[0]][0],
                )
                submit_btn = gr.Button('Run Task', interactive=False)

            with gr.Column():
                output = gr.Textbox(label='Output', lines=10, interactive=False)

        provider.change(fn=update_models_for, inputs=provider, outputs=model)

        task.change(fn=toggle_button, inputs=task, outputs=submit_btn)

        submit_btn.click(
            fn=lambda *args: asyncio.run(run_browser_task(*args)),
            inputs=[task, provider, model],
            outputs=output,
        )

    return interface


if __name__ == '__main__':
    demo = create_ui()
    demo.launch()
