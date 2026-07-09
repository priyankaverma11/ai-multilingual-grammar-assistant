
"""
Main FastAPI application for the Grammar Assistant API.
Provides endpoints for AI-powered grammar correction.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from grammar_service import correct_text
from models import GrammarRequest, GrammarResponse


app = FastAPI(
    title="Grammar Assistant API",
    description="AI-powered grammar correction for English, Hindi, and Hinglish.",
    version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/correct", response_model=GrammarResponse)
async def correct(request: GrammarRequest):
    return correct_text(request.text)