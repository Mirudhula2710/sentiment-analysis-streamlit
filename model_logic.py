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
    raw_results = pipe(text)
    
    # If the output is [[{...}]], we grab the first inner list
    if isinstance(raw_results, list) and len(raw_results) > 0:
        if isinstance(raw_results[0], list):
            return raw_results[0]
            
    return raw_results

def analyze_image(image):
    pipe = get_pipeline("image-classification")
    return pipe(image)

def transcribe_audio(audio_file):
    pipe = get_pipeline("automatic-speech-recognition")
    return pipe(audio_file)
