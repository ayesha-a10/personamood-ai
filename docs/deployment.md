Clone

↓

Create venv

↓

Install requirements

↓

Add .env

↓

Run FastAPI

↓

Run Streamlit

# Commands

git clone ...

cd personamood-ai

python -m venv venv

pip install -r requirements

uvicorn api.main:app --reload

streamlit run app/streamlit_app.py