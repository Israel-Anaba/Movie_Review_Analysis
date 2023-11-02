
import gradio as gr
import joblib
import pickle
import os
from text_preprocessing import process_text

# Define the path to your pickle file using forward slashes
components_path = 'src/assets/ML/sentiment_components.pkl'

# Check if the pickle file exists
if not os.path.exists(components_path):
    raise Exception(f"Pickle file '{components_path}' not found. Please check the file path.")

# Load the exported components using pickle
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

    # Define sentiment labels
    sentiment_labels = ['Negative', 'Positive']
   
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
