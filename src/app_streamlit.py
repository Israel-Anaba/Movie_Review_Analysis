import streamlit as st
import numpy as np
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

# Streamlit App with a light blue color theme
st.set_page_config(page_title="Movie Sentiment Analysis", page_icon="🎬", layout="wide")

# Set light blue color theme
st.markdown(
    """
    <style>
        .stApp {
            background-color: #ADD8E6;  /* Light Blue */
            color: #000000;
        }
        .stTextInput {
            color: #000000;
            background-color: #FFD700;  /* Gold */
        }
        .stButton {
            background-color: #FF6347;  /* Tomato */
            color: #000000;
        }
        .sidebar .sidebar-content {
            background-color: #87CEEB;  /* Sky Blue */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit App
st.title("Movie Review Sentiment Analysis 🤖👍 👎")

# Input text box for movie review
review_text = st.text_area("Enter a movie review...", "")

# Perform sentiment analysis when button is clicked
if st.button("Submit"):
    sentiment_scores = sent_analysis(review_text)

    # Display the sentiment scores
    st.write("Sentiment Scores:")
    for label, score in sentiment_scores.items():
        st.write(f"{label}: {score}")

    # Display the predicted sentiment label
    predicted_sentiment = max(sentiment_scores, key=sentiment_scores.get)
    st.write(f"Predicted Sentiment: {predicted_sentiment}")

# Sidebar with example reviews and additional information
st.sidebar.subheader("Example Reviews:")
st.sidebar.write("- I loved the movie! It was fantastic.")
st.sidebar.write("- The acting was terrible, and the plot was boring.")
st.sidebar.write("- This film is just okay. Not great, not terrible.")

st.sidebar.subheader("Additional Information:")
st.sidebar.markdown(
    """
    Explore this Movie Review Sentiment Analysis tool to classify the sentiment of movie reviews.
    Simply enter your movie review text and click the submit button to see the predicted sentiment.
    This Machine Learning model is designed to help you understand the sentiment conveyed in movie reviews, whether they are Positive OR Negative.
    [Check out the GitHub repository for more details.](https://github.com/Israel-Anaba/Movie_Review_Analysis/blob/main/src/app.py)
    """
)
