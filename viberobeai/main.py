import asyncio

import gradio as gr

from viberobeai.team import viberobe


def toggle_button(task):
    """Enable the button only if task is not empty."""
    return gr.Button(interactive=bool(task.strip()))


def create_ui():
    title = 'VibeRobe.ai - Your Personal Fashion Stylist'
    description = "Ask for outfit suggestions like 'What should I wear for a rooftop dinner in Bangalore?'"

    with gr.Blocks(title=title) as interface:
        gr.Markdown('# Viberobe AI')

        with gr.Row():
            with gr.Column():
                task = gr.Textbox(
                    label=description,
                    lines=3,
                )
                submit_btn = gr.Button('Run Task', interactive=False)

            with gr.Column():
                output = gr.Textbox(label='Output', lines=10, interactive=False)

        task.change(fn=toggle_button, inputs=task, outputs=submit_btn)

        submit_btn.click(
            fn=lambda *args: asyncio.run(viberobe(*args)),
            inputs=[task],
            outputs=output,
        )

    return interface


if __name__ == '__main__':
    demo = create_ui()
    demo.launch()
