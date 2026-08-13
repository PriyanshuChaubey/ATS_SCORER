#!/bin/bash
set -e

# Start FastAPI backend in the background
uvicorn backend.main:app --host 0.0.0.0 --port 8000 &

# Give the backend a moment to load models before frontend starts calling it
sleep 5

# Start Streamlit frontend in the foreground (keeps the container alive)
streamlit run frontend/streamlit_app.py --server.port=8501 --server.address=0.0.0.0