import streamlit as st
from PIL import Image
import model_logic as ml

st.set_page_config(page_title="AI Workstation", layout="wide")

st.sidebar.title("🛠️ AI Tools")
task = st.sidebar.selectbox("Choose Task", ["Sentiment", "Image Classify"])

st.title("🚀 Multi-Purpose AI Workstation")

if task == "Sentiment":
    user_input = st.text_area("Enter Text:", placeholder="e.g., The sun is a star.")
    
    if st.button("Analyze"):
        if user_input:
            with st.spinner('Calculating probabilities...'):
                # Get the full list of results
                # Add [0] at the end to "un-nest" the list
                results = ml.analyze_text(user_input)[0]
                
                # 1. Show the Bar Chart (Crucial for seeing 'Uncertainty')
                st.subheader("Confidence Breakdown")
                chart_data = {res['label'].capitalize(): res['score'] for res in results}
                st.bar_chart(chart_data)
                
                # 2. Show the Final Verdict
                top_res = results[0] # Highest score is always first
                label = top_res['label'].capitalize()
                score = top_res['score']
                
                if label == "Positive":
                    st.success(f"Verdict: {label} (Confidence: {score:.2f})")
                elif label == "Neutral":
                    st.info(f"Verdict: {label} (Confidence: {score:.2f})")
                else:
                    st.error(f"Verdict: {label} (Confidence: {score:.2f})")
        else:
            st.warning("Please enter some text first.")

elif task == "Image Classify":
    uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png'])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, width=300)
        if st.button("Identify"):
            res = ml.identify_image(img)
            st.json(res)
