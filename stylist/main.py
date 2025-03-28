import asyncio

import gradio as gr

from config import MODELS, PROVIDERS
from stylist.agent import run_task


def render_response(markdown_text):
    return gr.update(value=markdown_text), gr.update(value=markdown_text, visible=bool(markdown_text))


def update_models_for(provider):
    """Updates model choices based on selected provider."""
    return gr.Dropdown(choices=MODELS[provider], value=MODELS[provider][0])


def toggle_button(task):
    """Enable the button only if task is not empty."""
    return gr.Button(interactive=bool(task.strip()))


def create_ui():
    with gr.Blocks(title='Stylist') as interface:
        gr.Markdown('# Stylist Guide')

        with gr.Row():
            with gr.Column():
                task = gr.Textbox(
                    label="Ask for image suggestions like 'Smart-casual for rainy day office'",
                    placeholder='Smart-casual for rainy day office',
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
                output_image = gr.Image(visible=False)
                output_markdown = gr.Markdown()

        provider.change(fn=update_models_for, inputs=provider, outputs=model)

        task.change(fn=toggle_button, inputs=task, outputs=submit_btn)

        submit_btn.click(
            fn=lambda *args: render_response(asyncio.run(run_task(*args))),
            inputs=[task, provider, model],
            outputs=[output_markdown, output_image],
        )
    return interface


if __name__ == '__main__':
    demo = create_ui()
    demo.launch()
