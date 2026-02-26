import streamlit as st
from transformers import pipeline
import yaml

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

@st.cache_resource
def get_pipeline(task):
    """Loads and caches the heavy AI models."""
    model_id = config['models'].get(task)
    
    # top_k=None ensures we get scores for ALL labels (Pos/Neg/Neu)
    if task == "sentiment-analysis":
        return pipeline(task, model=model_id, top_k=None)
    
    return pipeline(task, model=model_id)

def analyze_text(text):
    pipe = get_pipeline("sentiment-analysis")
    raw_results = pipe(text)[0]
    
    # RoBERTa-latest mapping: 
    # LABEL_0 -> Negative, LABEL_1 -> Neutral, LABEL_2 -> Positive
    mapping = {"neutral": "Neutral", "positive": "Positive", "negative": "Negative"}
    
    # If the model uses labels like 'LABEL_0', we fix them here
    clean_results = []
    for res in raw_results:
        label = res['label'].lower()
        # Map technical labels to human words
        final_label = mapping.get(label, label)
        clean_results.append({"label": final_label, "score": res['score']})
        
    return clean_results

def analyze_image(image):
    pipe = get_pipeline("image-classification")
    return pipe(image)

def transcribe_audio(audio_file):
    pipe = get_pipeline("automatic-speech-recognition")
    return pipe(audio_file)
