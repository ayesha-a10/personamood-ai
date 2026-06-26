from chatbot import PersonaMoodChatbot

bot = PersonaMoodChatbot()

while True:

    text = input("\nYou: ")

    if text.lower() in ["exit", "quit"]:
        break

    result = bot.chat(text)

    print("\nDetected Personality")
    print(result["personality"])

    print("\nDetected Mood")
    print(result["mood"])

    print("\nPersonaMood-AI")
    print(result["response"])