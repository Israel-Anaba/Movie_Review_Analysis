
import gradio as gr
import joblib
import pickle
from text_preprocessing import process_text


# Load the exported components
components_path = r'src\assets\ML\sentiment_components.pkl'
with open(components_path, 'rb') as file:
    components_dict = pickle.load(file)


loaded_cleaner = components_dict['cleaner']
loaded_vectorizer = components_dict['cleaner_tfidf_vectorizer']
loaded_classifier = components_dict['cleaner_classifier']

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
    description="An AI model that predicts sentiment in movie reviews, providing labels for 'NEGATIVE' and 'POSITIVE' sentiments.",
    theme="default",
    live=True,
)


if __name__ == "__main__":
    demo.launch()
