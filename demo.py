import gradio as gr
from gradio.mix import Parallel, Series

io1 = gr.Interface.load("huggingface/EleutherAI/gpt-neo-1.3B")
io2 = gr.Interface.load("huggingface/t5-small")
io3 = gr.Interface.load("huggingface/facebook/bart-large-cnn")

title = "GPT-Neo, T5 and Bart Series Demo"
description = "demo for GPT-Neo, T5 and Bart Series Demo using Gradio Series. To use it, simply add your text, or click one of the examples to load them. Read more at the links below."
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/1910.10683'>Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer</a> | <a href='https://arxiv.org/abs/1910.13461'>BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension</a> | <a href='http://github.com/eleutherai/gpt-neo'>GPT-Neo: Large Scale Autoregressive Language Modeling with Mesh-Tensorflow</a></p>"
examples = [
    ['The tower is 324 metres (1,063 ft) tall,'],
    ["The Moon's orbit around Earth has"],
    ["The smooth Borealis basin in the Northern Hemisphere covers 40%"]
]
Series(io1,io2,io3, inputs=gr.inputs.Textbox(lines=5, label="Input Text"),title=title,description=description,article=article, examples=examples).launch()