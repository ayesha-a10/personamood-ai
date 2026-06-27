# 🧠 PersonaMood-AI

> An intelligent AI chatbot that personalizes conversations using **Big Five Personality Detection**, **Mood Detection**, **Prompt Engineering**, and **OpenAI GPT**.

---

# 📖 Overview

**PersonaMood-AI** is an adaptive conversational AI system designed to generate personalized responses by combining **Artificial Intelligence**, **Emotion Recognition**, and **Large Language Models**.

Unlike traditional chatbots that respond only to the current message, PersonaMood-AI analyzes:

- 🧠 User personality (Big Five/OCEAN)
- 😊 Current emotional state
- 💬 Conversation history
- 🎯 Prompt engineering strategies

These insights are used to tailor responses that are more engaging, context-aware, and personalized.

---

# ✨ Features

### 🧠 Personality Detection

- Big Five (OCEAN) personality prediction
- Logistic Regression classifier
- TF-IDF feature extraction
- Dynamic personality profile updates during conversations

### 😊 Mood Detection

- Logistic Regression classifier
- Detects emotions including:
  - Joy
  - Sadness
  - Anger
  - Fear
  - Love
  - Surprise
  - Neutral

### 🤖 Intelligent Prompt Engineering

- Personality-aware prompting
- Mood-aware prompting
- Adaptive response generation
- Context-sensitive conversation flow

### 💬 Conversation Memory

- Maintains recent conversation history
- Updates personality profile periodically
- Configurable memory size

### 🌐 Modern Application

- FastAPI backend
- Streamlit frontend
- OpenAI GPT integration
- REST API
- Developer Mode
- Download conversation
- Clear conversation

---

# 🏗 System Architecture

```text
                    User
                      │
                      ▼
             Streamlit Frontend
                      │
                      ▼
               FastAPI Backend
                      │
      ┌───────────────┴───────────────┐
      │                               │
      ▼                               ▼
Personality Classifier         Mood Detector
      │                               │
      └───────────────┬───────────────┘
                      ▼
            Conversation Memory
                      ▼
              Prompt Engineering
                      ▼
              OpenAI GPT Model
                      ▼
          Personalized AI Response
                      ▼
              Streamlit Interface
```

---

# 📂 Project Structure

```text
personamood-ai/
│
├── api/
│   └── main.py
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── prompts/
│
├── docs/
│   ├── project_blueprint.md
│   ├── data_pipeline.md
│   ├── deployment.md
│   ├── folder_explanation.md
│   └── model_architecture.md
│
├── models/
│   ├── personality_model/
│   └── emotion_model/
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_training.ipynb
│   ├── 04_evaluation.ipynb
│   ├── 05_personality_inference_pipeline.ipynb
│   └── 06_mood_detectin.ipynb
│
├── src/
│   ├── chatbot.py
│   ├── config.py
│   ├── conversation_memory.py
│   ├── mood_detector.py
│   ├── personality_classifier.py
│   ├── prompt_engine.py
│   ├── response_generator.py
│   └── utils.py
│
├── tests/
│
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

# 🛠 Tech Stack

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- Logistic Regression
- TF-IDF Vectorizer

## Deep Learning

- Hugging Face Transformers
- PyTorch

## Large Language Model

- OpenAI GPT

## Backend

- FastAPI
- Uvicorn

## Frontend

- Streamlit

## Data Processing

- Pandas
- NumPy

## Utilities

- Joblib
- Python-dotenv
- Requests

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/personamood-ai.git

cd personamood-ai
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# 🚀 Running the Application

## Start FastAPI

```bash
uvicorn api.main:app --reload
```

FastAPI documentation:

```
http://127.0.0.1:8000/docs
```

---

## Start Streamlit

```bash
streamlit run app/streamlit_app.py
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|----------|------------|-----------------------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| POST | `/chat` | Generate chatbot response |
| POST | `/clear` | Clear conversation memory |

---

# 📊 Model Performance

## Personality Detection (Current Baseline)

| Trait | Accuracy | F1 Score |
|--------|----------|-----------|
| Openness | 0.64 | 0.67 |
| Conscientiousness | 0.56 | 0.60 |
| Extraversion | 0.55 | 0.59 |
| Agreeableness | 0.55 | 0.63 |
| Neuroticism | 0.54 | 0.55 |

> These results correspond to the current Logistic Regression baseline and will be improved in future versions.

---

# 🔮 Future Improvements

- LangChain Integration
- Retrieval-Augmented Generation (RAG)
- ChromaDB / FAISS
- Fine-tuned Personality Models
- Improved Emotion Detection
- Long-term User Profiles
- Voice Input and Output
- Multi-language Support
- User Authentication

---

# Try Out Live
https://personamood-ai.onrender.com

---

# License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Feedback, suggestions, and contributions are always welcome.
