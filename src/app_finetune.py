import gradio as gr
import numpy as np
import pickle
from scipy.special import softmax
from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoConfig


# Requirements
model_path = "gr8testgad-1/movie_sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_path)
config = AutoConfig.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)


# Preprocess text (username and link placeholders)
def preprocess(text):
    # Split the text into words and process each word
    new_text = []

    # Replace usernames starting with '@' with '@user'
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t

        # Replace links starting with 'http' with 'http'
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

# Perform sentiment analysis on the preprocessed text
def sent_analysis(text):
    text = preprocess(text)

    # PyTorch-based models
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores_ = output[0][0].detach().numpy()
    scores_ = softmax(scores_)

    # Format output dict of scores
    labels = {0: 'NEGATIVE', 1: 'POSITIVE'}
    scores = {labels[i]: float(s) for i, s in enumerate(scores_)}
    return scores

# Create a Gradio interface
demo = gr.Interface(
    fn=sent_analysis,
    inputs=gr.Textbox(placeholder="Enter a movie review..."),
    outputs="label",
    interpretation="default",
    examples=[
        ["I loved the movie! It was fantastic."],
        ["The acting was terrible, and the plot was boring."],
        ["This film is just okay. Not great, not terrible."],
    ],
    title="Movie Review Sentiment Analysis 🤖👍 👎",
    description="""
    <p style='text-align: center'>Explore this Movie Review Sentiment Analysis tool to classify the sentiment of movie reviews .</p>
    <p style='text-align: center'>Simply enter your movie review text to see the predicted sentiment.</p>
    <p style='text-align: center'>This Machine Learning model is designed to help you understand the sentiment conveyed in movie reviews, whether they are Positive OR Negative.</p>
    <p style='text-align: center'><a href='https://github.com/Israel-Anaba/Movie_Review_Analysis/blob/main/src/app.py' target='_blank'>Check out the GitHub repository for more details.</a></p>
    """,
    theme="default",

    live=True,
)


if __name__ == "__main__":
    demo.launch()