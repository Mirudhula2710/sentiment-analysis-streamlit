import streamlit as st
from model_logic import get_sentiment

st.set_page_config(page_title="AI Sentiment Analyzer")

st.title("😊 Sentiment Analysis App")
st.write("Using Python, Hugging Face, and Streamlit.")

user_input = st.text_area("Type something here:")

if st.button("Analyze"):
    if user_input:
        with st.spinner('Thinking...'):
            result = get_sentiment(user_input)
            label = result['label']
            score = result['score']
            
        if label == "POSITIVE":
            st.success(f"Positive! (Confidence: {score:.2f})")
        else:
            st.error(f"Negative! (Confidence: {score:.2f})")
    else:
        st.warning("Please enter text first.")
          
