import streamlit as st
from transformers import pipeline
import yaml

# Load the configuration
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

@st.cache_resource
def get_pipeline():
    """Loads and caches the sentiment model with all labels enabled."""
    model_id = config['models'].get("sentiment")
    # top_k=None allows us to see the scores for ALL labels at once
    return pipeline("sentiment-analysis", model=model_id, top_k=None)

def analyze_text(text):
    pipe = get_pipeline()
    raw_results = pipe(text)
    
    # Standardize the list format to avoid TypeError on iPad
    if isinstance(raw_results, list) and len(raw_results) > 0:
        if isinstance(raw_results[0], list):
            return raw_results[0]
    return raw_results
