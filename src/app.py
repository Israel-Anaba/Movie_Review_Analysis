
import gradio as gr
import joblib
import pickle

# Load the exported components
with open("sentiment_components.pkl", 'rb') as file:
    loaded_components = pickle.load(file)

loaded_cleaner = loaded_components['cleaner']
loaded_vectorizer = loaded_components['cleaner_tfidf_vectorizer']
loaded_classifier = loaded_components['cleaner_classifier']

def sent_analysis(text):
    # Preprocess the input text using the loaded cleaner
    text = loaded_cleaner(text)
    
    # Vectorize the text using the loaded vectorizer
    X_tfidf = loaded_vectorizer.transform([text])
    
    # Make predictions using the loaded classifier
    prediction = loaded_classifier.predict(X_tfidf)[0]
    
    # Return the predicted sentiment label
    return prediction

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
    title="Movie Review Sentiment Analysis",
    description="An AI model that predicts sentiment in movie reviews, providing labels for 'NEGATIVE', 'NEUTRAL', and 'POSITIVE' sentiments.",
    theme="default",
    live=True,
)


if __name__ == "__main__":
    demo.launch()
