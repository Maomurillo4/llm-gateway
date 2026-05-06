import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI()
load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL_NAME = os.getenv("MODEL_NAME", "qwen2.5:0.5b")

class PromptRequest(BaseModel):
    prompt: str

@app.post("/chat/")
async def chat(request: PromptRequest):
    try:
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(OLLAMA_URL, json={
                "model": MODEL_NAME,
                "prompt": request.prompt,
                "stream": False
            })
            data = response.json()
            return {"response": data["response"]}
    except httpx.TimeoutException:
        raise HTTPException(504, "Ollama took too long")
    except httpx.ConnectError:
        raise HTTPException(503, "Unable to connect to Ollama")
    except Exception as e:
        raise HTTPException(500, str(e))