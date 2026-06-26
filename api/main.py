"""
FastAPI backend for PersonaMood-AI.
"""

from pathlib import Path
import sys

# Add src to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "src"

sys.path.append(str(SRC_DIR))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from chatbot import PersonaMoodChatbot
from config import OPENAI_MODEL
from utils import get_logger


logger = get_logger(__name__)


# ====================================================
# FastAPI App
# ====================================================

app = FastAPI(

    title="PersonaMood-AI",

    description="""
AI chatbot that adapts responses using

• Big Five Personality Detection

• Emotion Detection

• Prompt Engineering

• GPT-4.1-mini
""",

    version="1.0.0"

)

logger.info("Starting PersonaMood-AI API...")

bot = PersonaMoodChatbot()

logger.info("Chatbot loaded successfully.")


# ====================================================
# Request Models
# ====================================================

class ChatRequest(BaseModel):
    message: str


# ====================================================
# Response Models
# ====================================================

class ChatResponse(BaseModel):

    personality: dict

    mood: str

    response: str


# ====================================================
# Routes
# ====================================================

@app.get("/")
def root():

    return {

        "project": "PersonaMood-AI",

        "version": "1.0.0",

        "status": "Running"

    }


@app.get("/health")
def health():

    return {

        "status": "healthy",

        "model": OPENAI_MODEL

    }


@app.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    try:

        logger.info("Incoming chat request.")

        result = bot.chat(request.message)

        logger.info("Chat completed.")

        return ChatResponse(**result)

    except Exception as e:

        logger.exception("Chat failed.")

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )


@app.post("/clear")
def clear():

    bot.clear_memory()

    logger.info("Conversation memory cleared.")

    return {

        "message": "Conversation cleared successfully."

    }