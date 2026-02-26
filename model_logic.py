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
    return pipeline(task, model=model_id)

def analyze_text(text):
    pipe = get_pipeline("sentiment-analysis")
    return pipe(text)[0]

def analyze_image(image):
    pipe = get_pipeline("image-classification")
    return pipe(image)

def transcribe_audio(audio_file):
    pipe = get_pipeline("automatic-speech-recognition")
    return pipe(audio_file)
  
