import streamlit as st
from transformers import pipeline
import yaml

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

@st.cache_resource
def get_pipeline(task):
    # HARDCODE this for one run to force the download
    model_id = "cardiffnlp/twitter-roberta-base-sentiment-latest" 
    return pipeline(task, model=model_id, top_k=None)

def analyze_text(text):
    pipe = get_pipeline("sentiment-analysis")
    raw_results = pipe(text)
    
    # If the output is [[{...}]], we grab the first inner list
    if isinstance(raw_results, list) and len(raw_results) > 0:
        if isinstance(raw_results[0], list):
            return raw_results[0]
            
    return raw_results

def analyze_image(image):
    # This pulls the 'vision' model from your config.yaml
    pipe = get_pipeline("image-classification")
    
    # Returns the top 5 predictions by default
    results = pipe(image)
    return results

def transcribe_audio(audio_file):
    pipe = get_pipeline("automatic-speech-recognition")
    return pipe(audio_file)
