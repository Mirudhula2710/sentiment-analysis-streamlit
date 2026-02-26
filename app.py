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
                # Get the clean list of results
                results = ml.analyze_text(user_input)
                
                # Sort results so the highest score is first for the verdict
                results = sorted(results, key=lambda x: x['score'], reverse=True)
                
                # 1. Create Chart Data
                chart_data = {res['label'].capitalize(): res['score'] for res in results}
                
                # 2. Display Bar Chart
                st.subheader("Confidence Breakdown")
                st.bar_chart(chart_data)
                
                # 3. Show the Verdict
                top_res = results[0]
                label = top_res['label'].capitalize()
                score = top_res['score']
                
                if label == "Positive":
                    st.success(f"Verdict: {label} ({score:.2f})")
                elif label in ["Neutral", "Label_1"]: # Handles different model naming
                    st.info(f"Verdict: Neutral ({score:.2f})")
                else:
                    st.error(f"Verdict: Negative ({score:.2f})")
elif task == "Image Classify":
    # Allows both file upload and iPad camera use
    uploaded_file = st.file_uploader("Upload an Image", type=['jpg', 'jpeg', 'png'])
    camera_file = st.camera_input("Or take a photo")

    # Use whichever input is available
    input_image = uploaded_file or camera_file

    if input_image:
        img = Image.open(input_image)
        st.image(img, caption="Target Image", use_container_width=True)
        
        if st.button("Identify Object"):
            with st.spinner('Scanning...'):
                results = ml.analyze_image(img)
                
                # Display results as a clean list with progress bars
                st.subheader("Results:")
                for res in results:
                    col1, col2 = st.columns([1, 2])
                    col1.write(res['label'])
                    col2.progress(res['score'])
