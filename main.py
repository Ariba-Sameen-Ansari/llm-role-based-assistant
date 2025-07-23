from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from role_logic import get_response_from_openai
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

class Query(BaseModel):
    role: str
    question: str

@app.post("/ask")
async def ask(query: Query):
    try:
        response = get_response_from_openai(query.role, query.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
