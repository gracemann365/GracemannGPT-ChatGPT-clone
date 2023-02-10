import os
import openai
import gradio as gr


openai.api_key = "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"

start_sequence = "\nChatbot:"
restart_sequence = "\nHuman: "

prompt = "This is the first prototype of my ChatGPT clone using OpenAI's text-davinci-003 dubbed ChatGPT 3.5 and Gradio"

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>GracemannGPT</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])
    
with gr.Blocks(css=".gradio-container {background-color: red}") as demo:
    ...

block.launch(debug = True)