import streamlit
from transformers import pipeline

st.title("Analyseur de Sentiments")

text = st.text_input("Entrez le texte à analyser :")

sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

if text:
    result = sentiment_analyzer(texte)[0]
    st.write(f"Label: {resultat['label']}, Score: {resultat['score']:.4f}")