FROM python:3.11-slim

# System dependencies:
# - libmagic1: needed by python-magic for file-type detection
# - libcairo2, libpango-1.0-0, libpangocairo-1.0-0, libgdk-pixbuf2.0-0, libffi-dev, shared-mime-info:
#   needed by WeasyPrint for PDF generation
RUN apt-get update && apt-get install -y --no-install-recommends \
    libmagic1 \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf-xlib-2.0-0 \
    libffi-dev \
    shared-mime-info \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --default-timeout=300 --no-cache-dir -r requirements.txt

RUN python -m spacy download en_core_web_md

COPY backend/ ./backend/
COPY frontend/ ./frontend/

COPY start.sh .
RUN chmod +x start.sh

EXPOSE 8000 8501

CMD ["./start.sh"]