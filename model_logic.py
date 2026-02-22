from transformers import pipeline

def get_sentiment(text):
    # This downloads the model from Hugging Face automatically
    classifier = pipeline("sentiment-analysis")
    result = classifier(text)
    return result[0]
  
