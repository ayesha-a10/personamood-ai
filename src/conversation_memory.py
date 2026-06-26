"""
Conversation memory module.
"""

from collections import deque


class ConversationMemory:

    def __init__(self, max_history=10):

        self.history = deque(maxlen=max_history)

        self.user_messages = []

    def add_user(self, message):

        self.history.append(
            {
                "role": "user",
                "content": message
            }
        )

        self.user_messages.append(message)

    def add_assistant(self, message):

        self.history.append(
            {
                "role": "assistant",
                "content": message
            }
        )

    def get_history(self):

        return list(self.history)

    def get_user_text(self):

        return "\n".join(self.user_messages)

    def get_message_count(self):

        return len(self.user_messages)

    def clear(self):

        self.history.clear()

        self.user_messages.clear()