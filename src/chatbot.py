"""
Main chatbot pipeline.
"""

from config import (
    MAX_HISTORY,
    PERSONALITY_UPDATE_INTERVAL,
)

from conversation_memory import ConversationMemory
from mood_detector import MoodDetector
from personality_classifier import PersonalityClassifier
from prompt_engine import PromptEngine
from response_generator import ResponseGenerator

from utils import get_logger


logger = get_logger(__name__)


class PersonaMoodChatbot:

    def __init__(self):

        logger.info("Initializing PersonaMood-AI...")

        self.memory = ConversationMemory(
            max_history=MAX_HISTORY
        )

        self.personality = PersonalityClassifier()

        self.mood = MoodDetector()

        self.prompt_engine = PromptEngine()

        self.generator = ResponseGenerator()

        self.personality_profile = None

        logger.info("Initialization complete.")

    def _update_personality(self, message):

        if self.personality_profile is None:

            logger.info("Creating initial personality profile.")

            self.personality_profile = (
                self.personality.predict_scores(message)
            )

            return

        if (
            self.memory.get_message_count()
            % PERSONALITY_UPDATE_INTERVAL
            == 0
        ):

            logger.info("Refreshing personality profile.")

            text = self.memory.get_user_text()

            self.personality_profile = (
                self.personality.predict_scores(text)
            )

    def chat(self, message):

        logger.info("New user message received.")

        # Store user message first
        self.memory.add_user(message)

        # Stable personality
        self._update_personality(message)

        personality = self.personality_profile

        # Current mood
        mood = self.mood.predict(message)

        # Build prompt
        system_prompt = self.prompt_engine.build_prompt(
            personality,
            mood
        )

        # Generate response
        response = self.generator.generate(
            system_prompt=system_prompt,
            user_message=message,
            history=self.memory.get_history()
        )

        # Store assistant response
        self.memory.add_assistant(response)

        logger.info("Response generated successfully.")

        return {
            "personality": personality,
            "mood": mood,
            "response": response
        }

    def clear_memory(self):

        logger.info("Conversation cleared.")

        self.memory.clear()

        self.personality_profile = None