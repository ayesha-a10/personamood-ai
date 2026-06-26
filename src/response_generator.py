"""
OpenAI response generator.
"""

from openai import OpenAI

from config import (
    OPENAI_API_KEY,
    OPENAI_MODEL,
    TEMPERATURE,
    MAX_TOKENS
)

from utils import get_logger


logger = get_logger(__name__)


class ResponseGenerator:

    def __init__(self):

        if not OPENAI_API_KEY:

            raise ValueError("OPENAI_API_KEY not found.")

        self.client = OpenAI(
            api_key=OPENAI_API_KEY.strip()
        )

        self.model = OPENAI_MODEL

        logger.info("ResponseGenerator initialized.")

    def generate(

        self,

        system_prompt,

        user_message,

        history=None,

        temperature=TEMPERATURE,

        max_tokens=MAX_TOKENS

    ):

        if history is None:

            history = []

        messages = [

            {

                "role": "system",

                "content": system_prompt

            }

        ]

        messages.extend(history)

        messages.append(

            {

                "role": "user",

                "content": user_message

            }

        )

        logger.info("Sending request to OpenAI...")

        response = self.client.chat.completions.create(

            model=self.model,

            messages=messages,

            temperature=temperature,

            max_tokens=max_tokens

        )

        logger.info("Response received.")

        return response.choices[0].message.content.strip()