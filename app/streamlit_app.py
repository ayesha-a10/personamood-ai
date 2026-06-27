"""
PersonaMood-AI Streamlit Frontend
"""

import streamlit as st
import requests

# ==========================================================
# Configuration
# ==========================================================

BASE_URL = "https://personamood-api.onrender.com"

CHAT_URL = f"{BASE_URL}/chat"
CLEAR_URL = f"{BASE_URL}/clear"
HEALTH_URL = f"{BASE_URL}/health"

st.set_page_config(
    page_title="PersonaMood-AI",
    page_icon="🧠",
    layout="wide"
)

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.title("🧠 PersonaMood-AI")

    st.markdown(
        """
An AI assistant that adapts responses using

- Personality Detection
- Mood Detection
- Prompt Engineering
- GPT
"""
    )

    st.divider()

    developer_mode = st.toggle(
        "Developer Mode",
        value=False
    )

    st.divider()

    try:

        health = requests.get(HEALTH_URL).json()

        st.success("Backend Connected")

        st.caption(f"Model: {health['model']}")

    except Exception:

        st.error("Backend Offline")

    st.divider()

    if st.button("🗑 Clear Conversation"):

        requests.post(CLEAR_URL)

        st.session_state.messages = []

        st.rerun()

# ==========================================================
# Session State
# ==========================================================

if "messages" not in st.session_state:

    st.session_state.messages = []

# ==========================================================
# Title
# ==========================================================

st.title("🧠 PersonaMood-AI")

st.caption(
    "Adaptive AI Chatbot powered by Personality + Mood Detection"
)

# ==========================================================
# Display Chat History
# ==========================================================

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

        if developer_mode and msg["role"] == "assistant":

            if "debug" in msg:

                with st.expander("Developer Insights"):

                    st.write("Mood")

                    st.success(msg["debug"]["mood"])

                    st.write("Personality")

                    st.json(msg["debug"]["personality"])

# ==========================================================
# Chat Input
# ==========================================================

user_input = st.chat_input(
    "Type your message..."
)

if user_input:

    st.session_state.messages.append(

        {

            "role": "user",

            "content": user_input

        }

    )

    with st.chat_message("user"):

        st.markdown(user_input)

    with st.spinner("Thinking..."):

        response = requests.post(

            CHAT_URL,

            json={

                "message": user_input

            }

        )

    if response.status_code == 200:

        result = response.json()

        assistant_text = result["response"]

        personality = result["personality"]

        mood = result["mood"]

    else:

        assistant_text = "Backend Error"

        personality = {}

        mood = "unknown"

    with st.chat_message("assistant"):

        st.markdown(assistant_text)

        if developer_mode:

            with st.expander("Developer Insights"):

                st.write("Mood")

                st.success(mood)

                st.write("Personality")

                st.json(personality)

    st.session_state.messages.append(

        {

            "role": "assistant",

            "content": assistant_text,

            "debug": {

                "personality": personality,

                "mood": mood

            }

        }

    )

# ==========================================================
# Download Conversation
# ==========================================================

st.divider()

conversation = ""

for msg in st.session_state.messages:

    conversation += f"{msg['role'].upper()}:\n"

    conversation += msg["content"]

    conversation += "\n\n"

st.download_button(

    "📥 Download Conversation",

    conversation,

    file_name="conversation.txt"

)