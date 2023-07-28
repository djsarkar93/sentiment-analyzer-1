import nltk
import textblob
import re


nltk.download('wordnet')


def analyze(text):
    # Keeping only text and digits
    text = re.sub(r'[^A-Za-z0-9]', ' ', text)
    # Removes whitespaces
    text = re.sub(r"\'s", ' ', text)
    # Removing links if any
    text = re.sub(r'http\S+', ' link ', text)
    # Removes punctuations and numbers
    text = re.sub(r'\b\d+(?:\.\d+)?\s+', '', text)
    # Splitting text into words
    words = text.split()
    # Initializing the WordNet lemmatizer
    lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()
    # Lematizing the words and joining them back to text
    lemmatized_words =[lemmatizer.lemmatize(word) for word in words]
    lemmatized_text = " ".join(lemmatized_words)
    
    blob = textblob.TextBlob(lemmatized_text)
    return blob.sentiment.polarity
