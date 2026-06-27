"""
Central configuration for PersonaMood-AI.
"""

import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


# ==========================================
# OpenAI
# ==========================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OPENAI_MODEL = "gpt-4.1-mini"


# ==========================================
# Conversation
# ==========================================

MAX_HISTORY = 10

PERSONALITY_UPDATE_INTERVAL = 5


# ==========================================
# Generation
# ==========================================

TEMPERATURE = 0.7

MAX_TOKENS = 400


# ==========================================
# Personality
# ==========================================

PERSONALITY_THRESHOLD = 0.55


# ==========================================
# Mood
# ==========================================

DEFAULT_MOOD = "neutral"