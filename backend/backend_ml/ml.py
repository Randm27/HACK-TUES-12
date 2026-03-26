import gradio as gr
from transformers import AutoImageProcessor
from transformers import SiglipForImageClassification
from transformers.image_utils import load_image
from PIL import Image
import torch
import requests
from io import BytesIO
import numpy as np

# Load model and processor
model_name = "prithivMLmods/Hand-Gesture-19"
model = SiglipForImageClassification.from_pretrained(model_name)
processor = AutoImageProcessor.from_pretrained(model_name)

def hand_gesture_classification(image):
    """Predicts the hand gesture category from an image."""
    image = Image.fromarray(image).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.nn.functional.softmax(logits, dim=1).squeeze().tolist()
    
    labels = {
        "0": "call", 
        "1": "dislike", 
        "2": "fist", 
        "3": "four", 
        "4": "like", 
        "5": "mute", 
        "6": "no_gesture", 
        "7": "ok", 
        "8": "one", 
        "9": "palm", 
        "10": "peace", 
        "11": "peace_inverted", 
        "12": "rock", 
        "13": "stop", 
        "14": "stop_inverted", 
        "15": "three", 
        "16": "three2", 
        "17": "two_up", 
        "18": "two_up_inverted"
    }
    predictions = {labels[str(i)]: round(probs[i], 3) for i in range(len(probs))}
    
    return predictions

def read_image_url(image_url):
    response = requests.get(image_url)
    image_data = np.asarray(Image.open(BytesIO(response.content)))
    return image_data

def gesture_from_url(image_url):
    return hand_gesture_classification(read_image_url(image_url))

def get_gesture(image_url):
    predictions = gesture_from_url(image_url)
    return list(sorted(list(predictions.items()), key = lambda x:x[1], reverse=1))[0][0]

print(get_gesture("https://pnglove.com/data/img/1908_mSc9.jpg"))