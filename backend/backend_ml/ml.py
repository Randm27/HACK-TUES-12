import gradio as gr
from transformers import AutoImageProcessor
from transformers import SiglipForImageClassification
from transformers.image_utils import load_image
from PIL import Image
import torch
import requests
from io import BytesIO
import numpy as np
import base64

# Load model and processor
model_name = "my_gesture_model"
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
        "0": "y", 
        "1": "dislike", 
        "2": "a", 
        "3": "four", 
        "4": "like", 
        "5": "mute", 
        "6": "no_gesture", 
        "7": "c", 
        "8": "d", 
        "9": "palm", 
        "10": "k", 
        "11": "peace_inverted", 
        "12": "rock", 
        "13": "s", 
        "14": "stop_inverted", 
        "15": "w", 
        "16": "three2", 
        "17": "h", 
        "18": "two_up_inverted"
    }
    predictions = {labels[str(i)]: round(probs[i], 3) for i in range(len(probs))}
    
    return predictions

def sort_predictions(predictions):
    print(predictions)
    return list(sorted(list(predictions.items()), key = lambda x:x[1], reverse=1))[0][0]


def from_base64_string(base64_string):
    if "data:image" in base64_string:
        base64_string = base64_string.split(",")[1]
    return sort_predictions(hand_gesture_classification(np.asarray(Image.open(BytesIO(base64.b64decode(base64_string))))))