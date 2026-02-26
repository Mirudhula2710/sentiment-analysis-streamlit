import streamlit as st
import model_logic as ml

st.set_page_config(page_title="AI Sentiment Workstation", layout="wide")

# Header section
st.title("🚀 AI Sentiment Workstation")
st.markdown("Analyze text to see a nuanced breakdown of **Positive**, **Neutral**, and **Negative** emotions.")

# Input area
user_input = st.text_area("Enter Text:", placeholder="Type a fact or a sentence here...", height=150)

if st.button("Analyze Sentiment"):
    if user_input:
        with st.spinner('Calculating probabilities...'):
            # 1. Fetch results from the AI logic
            results = ml.analyze_text(user_input)
            
            # 2. Sort results (highest confidence first)
            results = sorted(results, key=lambda x: x['score'], reverse=True)
            
            # 3. Create and display the Bar Chart
            st.subheader("Confidence Breakdown")
            chart_data = {res['label'].capitalize(): res['score'] for res in results}
            st.bar_chart(chart_data)
            
            # 4. Display the Final Verdict with specific colors
            top_res = results[0]
            label = top_res['label'].capitalize()
            score = top_res['score']
            
            if label == "Positive":
                st.success(f"Verdict: {label} (Confidence: {score:.2f})")
            elif label in ["Neutral", "Label_1"]:
                st.info(f"Verdict: Neutral (Confidence: {score:.2f})")
            else:
                st.error(f"Verdict: Negative (Confidence: {score:.2f})")
    else:
        st.warning("Please enter some text before clicking Analyze.")

# Visual Footer
st.divider()
st.caption("Optimized for iPad Workstations | Powered by RoBERTa-Latest")
