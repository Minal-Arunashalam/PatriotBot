import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
import numpy as py


import bs4 as bs
import urllib.request
import re
from ai import primeAI, AI
# import gradio as gr

def get_info(page):
    link = urllib.request.urlopen(page)
    link = link.read()

    data = bs.BeautifulSoup(link, 'lxml')
    # print(data)

    data_paragraphs = data.find_all('p')
    data_text = ''
    for para in data_paragraphs:
        data_text += para.text

    # print(data_text)
    data_text = data_text.lower()

    data_text = re.sub(r'\[[0-9]*\]', ' ', data_text)
    data_text = re.sub(r'\s+', ' ', data_text)
    # print(data_text)

    sentence = nltk.sent_tokenize(data_text)
    words = nltk.word_tokenize(data_text)
    # print(words)
    # print(data_text)
    return data_text

def respond(question):
    #primeAI(site_text)
    output = AI(question)
    return output

# output = AI(data_text)
# print(output)


# with gr.Blocks(theme=gr.themes.Soft(), button_color="rgb(79, 70, 221)") as demo:
#     gr.Markdown(
#     """
#     # Patriot Bot
#     about me.
#     """)
#     #with gr.Tab("Write code"):
#     user_input = gr.Textbox(label="Enter your question!")
#     bot_output = gr.Textbox(label="Response")
#     button = gr.Button("meeenaaaal yaaaaaar")
#     # with gr.Tab("Explain code"):
#     #     filepath_input = gr.Textbox(label="If you want to upload a file for me to read, please enter the file path so I can access it")
#     #     upload_button = gr.Button("Send file path to assistant")
#     #     explain_input = gr.Textbox(label="What would you like me to explain?")
#     #     explain_output = gr.Textbox(label="My response")
#     #     explain_button = gr.Button("Explain")

#     # with gr.Accordion("Open for More!"):
#     #     gr.Markdown("Look at me...")

#     button.click(AI, inputs=user_input, outputs=bot_output)


# demo.launch(share=True)
