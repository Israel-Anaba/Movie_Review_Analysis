# text_preprocessing.py

import spacy
import string

nlp = spacy.load("en_core_web_sm")
stopwords = set(spacy.lang.en.STOP_WORDS)
punctuations = string.punctuation

def process_text(text):
    doc = nlp(text)
    tokens = [token.text for token in doc if token.text not in stopwords and token.text not in punctuations]
    return ' '.join(tokens)
