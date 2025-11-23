import streamlit as st
from transformers import pipeline

st.title("Analyseur de Sentiments")

text = st.text_input("Entrez le texte à analyser :")

sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

if text:
    result = sentiment_analyzer(text)[0]
    st.write(f"Label: {result['label']}, Score: {result['score']:.4f}")