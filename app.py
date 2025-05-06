import streamlit as st
from spelling_corrector import SpellingCorrector

corrector = SpellingCorrector()

st.title("📝 Spelling Corrector")

input_text = st.text_area("Enter your text:")

if st.button("Correct"):
    corrected = corrector.correct_text(input_text)
    st.success(f"Corrected Text:\n\n{corrected}")