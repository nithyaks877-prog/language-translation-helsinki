import sys
import streamlit as st
from transformers import pipeline

st.title("Language Translator Chatbot")

# Map readable names to language codes
languages = {
    "French": "fr",
    "German": "de",
    "Hindi": "hi",  
    "Spanish": "es"
}

# Input fields
text = st.text_area("Enter text to translate")
src = st.selectbox("Source Language", ["English"])  # fixed to English for now
tgt_name = st.selectbox("Target Language", list(languages.keys()))
tgt = languages[tgt_name]  # Get language code

if st.button("Translate"):
    src_code = "en"  # Since source is English for now
    model_name = f"Helsinki-NLP/opus-mt-{src_code}-{tgt}"
    translator = pipeline("translation", model=model_name)
    result = translator(text)[0]["translation_text"]
    st.success(result)
