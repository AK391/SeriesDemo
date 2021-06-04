import gradio as gr
from gradio.mix import Parallel, Series

io1 = gr.Interface.load("huggingface/EleutherAI/gpt-neo-1.3B")
io2 = gr.Interface.load("huggingface/t5-small")
io3 = gr.Interface.load("huggingface/facebook/bart-large-cnn")
Series(io1,io2,io3, inputs=gr.inputs.Textbox(lines=5, label="Input Text")).launch()