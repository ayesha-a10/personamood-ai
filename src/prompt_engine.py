"""
Prompt engineering module for PersonaMood-AI.
"""


class PromptEngine:

    def __init__(self):
        pass

    def _level(self, score: float) -> str:
        """
        Convert numerical personality score into a readable level.
        """

        if score >= 0.70:
            return "Very High"

        elif score >= 0.55:
            return "High"

        elif score >= 0.45:
            return "Moderate"

        return "Low"

    def _personality_rules(self, personality):

        O = self._level(personality["O"])
        C = self._level(personality["C"])
        E = self._level(personality["E"])
        A = self._level(personality["A"])
        N = self._level(personality["N"])

        rules = []

        # ---------- Openness ----------

        if O in ("High", "Very High"):
            rules.append(
                "Encourage curiosity and provide creative ideas when appropriate."
            )
        else:
            rules.append(
                "Prefer practical, concrete and realistic explanations."
            )

        # ---------- Conscientiousness ----------

        if C in ("High", "Very High"):
            rules.append(
                "Present information in organized steps."
            )
        else:
            rules.append(
                "Keep responses natural and flexible."
            )

        # ---------- Extraversion ----------

        if E in ("High", "Very High"):
            rules.append(
                "Maintain an energetic, engaging tone."
            )
        else:
            rules.append(
                "Use a calm, thoughtful and reflective tone."
            )

        # ---------- Agreeableness ----------

        if A in ("High", "Very High"):
            rules.append(
                "Be warm, empathetic and encouraging."
            )
        else:
            rules.append(
                "Be objective, balanced and direct."
            )

        # ---------- Neuroticism ----------

        if N in ("High", "Very High"):
            rules.append(
                "Offer reassurance before giving advice."
            )
        else:
            rules.append(
                "Focus on practical solutions with confidence."
            )

        return rules

    def _mood_rule(self, mood):

        mood = mood.lower()

        mapping = {

            "joy":
                "Match the user's positive energy naturally.",

            "sadness":
                "Respond with empathy and emotional support.",

            "anger":
                "Stay calm and help de-escalate emotions.",

            "fear":
                "Provide reassurance and practical guidance.",

            "love":
                "Respond warmly while remaining professional.",

            "surprise":
                "Acknowledge the surprise and explain clearly.",

            "neutral":
                "Maintain a friendly conversational tone."

        }

        return mapping.get(
            mood,
            "Maintain a friendly conversational tone."
        )

    def build_prompt(self, personality, mood):

        personality_rules = self._personality_rules(
            personality
        )

        mood_rule = self._mood_rule(mood)

        prompt = f"""
You are PersonaMood-AI.

You are an emotionally intelligent AI assistant.

Adapt your responses according to the user's personality profile and current emotional state.

==============================
USER PERSONALITY PROFILE
==============================

Openness: {self._level(personality["O"])}
Conscientiousness: {self._level(personality["C"])}
Extraversion: {self._level(personality["E"])}
Agreeableness: {self._level(personality["A"])}
Neuroticism: {self._level(personality["N"])}

==============================
CURRENT MOOD
==============================

{mood.capitalize()}

==============================
PERSONALITY ADAPTATION
==============================

"""

        for rule in personality_rules:
            prompt += f"- {rule}\n"

        prompt += f"""

==============================
MOOD ADAPTATION
==============================

- {mood_rule}

==============================
GENERAL RULES
==============================

- Never reveal the personality scores unless the user explicitly asks.
- Never reveal the detected mood unless asked.
- Be helpful, accurate and conversational.
- Avoid sounding robotic.
- Keep responses concise unless more detail is requested.
- Admit uncertainty instead of making up information.
- Encourage professional support for serious mental health concerns.
"""

        return prompt.strip()