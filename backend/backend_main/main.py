from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from Speech_to_text import transcribe_audio
from fastapi import FastAPI, File, UploadFile
import shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5000/","singspeak.org","*"],  # или ["http://127.0.0.1:5000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# model_name = "sshleifer/distilbart-cnn-12-6"
model_name = "sshleifer/distilbart-cnn-12-3"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

class TextRequest(BaseModel):
    text: str

def simplify_text(text):
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    outputs = model.generate(
        **inputs,
        max_length=100,
        min_length=30,
        do_sample=False
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

@app.post("/simplify")
def simplify(req: TextRequest):
    result = simplify_text(req.text)
    return {"simplified": result}

@app.post("/tts")
async def receive_audio(audio_data: UploadFile = File(...)):
    print(audio_data)
    file_path=f"./uploads/{audio_data.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(audio_data.file, buffer)
    
    return transcribe_audio(file_path)
