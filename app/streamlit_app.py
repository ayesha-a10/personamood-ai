"""
PersonaMood-AI Streamlit Frontend
Single Deployment Version
"""

import sys
from pathlib import Path

import streamlit as st

# ----------------------------------------------------
# Import chatbot
# ----------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.append(str(SRC_PATH))

from chatbot import PersonaMoodChatbot

# ----------------------------------------------------
# Streamlit Config
# ----------------------------------------------------

st.set_page_config(
    page_title="PersonaMood-AI",
    page_icon="🧠",
    layout="wide"
)

# ----------------------------------------------------
# Session State
# ----------------------------------------------------

if "bot" not in st.session_state:
    st.session_state.bot = PersonaMoodChatbot()

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

with st.sidebar:

    st.title("🧠 PersonaMood-AI")

    st.markdown("""
### AI Features

- Personality Detection
- Mood Detection
- Prompt Engineering
- GPT Response Generation
""")

    developer_mode = st.toggle(
        "Developer Mode",
        value=False
    )

    st.success("🟢 Chatbot Ready")

    if st.button("🗑 Clear Conversation"):

        st.session_state.bot.clear_memory()

        st.session_state.messages = []

        st.rerun()

# ----------------------------------------------------
# Main Page
# ----------------------------------------------------

st.title("🧠 PersonaMood-AI")

st.caption(
    "Adaptive AI Chatbot powered by Personality + Mood Detection"
)

# ----------------------------------------------------
# Previous Messages
# ----------------------------------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

        if (
            developer_mode
            and msg["role"] == "assistant"
            and "debug" in msg
        ):

            with st.expander("Developer Insights"):

                st.write("Detected Mood")

                st.success(msg["debug"]["mood"])

                st.write("Detected Personality")

                st.json(msg["debug"]["personality"])

# ----------------------------------------------------
# Chat Input
# ----------------------------------------------------

prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):

        try:

            result = st.session_state.bot.chat(prompt)

            assistant = result["response"]

            mood = result["mood"]

            personality = result["personality"]

        except Exception as e:

            assistant = f"❌ {str(e)}"

            mood = "unknown"

            personality = {}

    with st.chat_message("assistant"):

        st.markdown(assistant)

        if developer_mode:

            with st.expander("Developer Insights"):

                st.write("Detected Mood")

                st.success(mood)

                st.write("Detected Personality")

                st.json(personality)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant,
            "debug": {
                "mood": mood,
                "personality": personality
            }
        }
    )

# ----------------------------------------------------
# Download Conversation
# ----------------------------------------------------

st.divider()

conversation = ""

for msg in st.session_state.messages:

    conversation += (
        f"{msg['role'].upper()}:\n"
        f"{msg['content']}\n\n"
    )

st.download_button(
    "📥 Download Conversation",
    conversation,
    file_name="conversation.txt",
    mime="text/plain"
)