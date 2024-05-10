from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from transformers import AutoTokenizer, LlamaForCausalLM
import transformers

app = FastAPI()

# Define Pydantic model for request
class ChatRequest(BaseModel):
    message: str

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-step-50K-105b")
model = LlamaForCausalLM.from_pretrained("keeeeenw/MicroLlama")
from huggingface_hub import login
import torch
import transformers
from transformers import AutoTokenizer, LlamaForCausalLM

login(token="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")
@app.post("/send_message")


# Serve HTML directly from FastAPI
@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

# Mount the static directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")
