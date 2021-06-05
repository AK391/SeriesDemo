import gradio as gr
from gradio.mix import Parallel, Series

io1 = gr.Interface.load("huggingface/EleutherAI/gpt-neo-1.3B")
io2 = gr.Interface.load("huggingface/facebook/m2m100_418M")

title = "GPT-Neo and M2M Series Demo"
description = "demo for GPT-Neo and M2M using Gradio Series for text generation and translation. To use it, simply add your text, or click one of the examples to load them. Read more at the links below."
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/2010.11125'>Beyond English-Centric Multilingual Machine Translation</a> | <a href='http://github.com/eleutherai/gpt-neo'>GPT-Neo: Large Scale Autoregressive Language Modeling with Mesh-Tensorflow</a></p>"
examples = [
    ['The tower is 324 metres (1,063 ft) tall,'],
    ["The Moon's orbit around Earth has"],
    ["The smooth Borealis basin in the Northern Hemisphere covers 40%"]
]
Series(io1,io2, inputs=gr.inputs.Textbox(lines=5, label="Input Text"),title=title,description=description,article=article, examples=examples).launch()