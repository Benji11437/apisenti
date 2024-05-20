from textblob import TextBlob
import re, nltk
nltk.download("stopwords")
from deep_translator import GoogleTranslator
from sklearn.feature_extraction.text import TfidfVectorizer

text :str


def cleaned_text(text: str):
    text = str(text)
    clean = re.sub(r"\n", " ", text)
    clean = clean.lower()
    clean = re.sub(r"[~.,%/:;?_&+*=!-]", " ", clean)
    clean = re.sub(r"[^a-z]", " ", clean)
    clean = clean.strip()
    clean = re.sub(r"\s{2,}", " ", clean)
    return clean


def vectorize_text_column(text_column):
   
    # Initialisation du vectoriseur TF-IDF
    vectorizer = TfidfVectorizer()
    # Appliquer le vectoriseur sur la colonne de texte
    features = vectorizer.fit_transform(text_column)
    # Convertir les caractéristiques en une représentation de matrice dense
    features_dense = features.toarray()
    return features_dense