import streamlit as st
from PIL import Image
import model_logic as ml

st.set_page_config(page_title="AI Workstation", layout="wide")

# 1. Sidebar for History and Settings
st.sidebar.title("Settings & History")
task = st.sidebar.selectbox("Choose Task", ["Sentiment", "Image Classify", "Audio Transcribe"])

# 2. Main Interface
st.title("🚀 Multi-Purpose AI Workstation")

if task == "Sentiment":
    user_input = st.text_area("Enter Text:")
    if st.button("Analyze") and user_input:
        res = ml.analyze_text(user_input)
        st.write(f"Result: {res['label']} ({res['score']:.2f})")

elif task == "Image Classify":
    uploaded_file = st.file_uploader("Upload an Image", type=['jpg', 'png', 'jpeg'])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", width=300)
        if st.button("Identify"):
            res = ml.analyze_image(img)
            st.json(res)

# (Add similar logic for Audio using st.audio_input)
