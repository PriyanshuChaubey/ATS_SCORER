# 🎯 ATS Resume Scorer

An AI-powered resume analysis tool that scores resumes against real ATS (Applicant Tracking System) criteria, validates claimed skills against actual project/experience evidence using semantic AI matching, and compares resumes against job descriptions — with detailed, actionable feedback and downloadable PDF reports.

## ✨ Features

- **ATS Score (0–100)** — weighted scoring across 5 categories: Formatting, Keywords & Skills, Content Quality, Skill Validation, and ATS Compatibility
- **AI-Powered Skill Validation** — uses Sentence-BERT semantic similarity to verify that claimed skills are genuinely backed by project or work experience, even when worded differently
- **Job Description Matching** — semantic + keyword-based comparison between a resume and a target job description, including missing keywords and skills gap analysis
- **Detailed, Actionable Feedback** — every detected issue includes severity, ATS impact, explanation, and a concrete before/after fix example
- **PDF Report Export** — generates a polished, multi-page PDF report of the full analysis
- **User Accounts & History** — sign in with email/password or Google OAuth; every analysis is saved to your account and viewable later
- **Secure, User-Scoped Data** — JWT-based authentication ensures users can only access their own analysis history

## 🛠️ Tech Stack

**Backend:** FastAPI, spaCy, Sentence-Transformers, Groq (LLM), PyJWT
**Frontend:** Streamlit
**Database & Auth:** Supabase (PostgreSQL + Auth)
**File Parsing:** pdfplumber, PyPDF2, python-docx
**PDF Generation:** Jinja2 + WeasyPrint
**Fuzzy Matching:** RapidFuzz

## 🏗️ Architecture

```
┌─────────────┐      REST API       ┌─────────────┐
│  Streamlit  │ ──────────────────► │   FastAPI   │
│  Frontend   │ ◄────────────────── │   Backend   │
└─────────────┘                     └──────┬──────┘
                                            │
                    ┌───────────────────────┼────────────────────┐
                    ▼                       ▼                    ▼
              ┌──────────┐           ┌─────────────┐      ┌────────────┐
              │  Groq    │           │   spaCy +   │      │  Supabase  │
              │  (LLM)   │           │ Sentence-BERT│     │ (DB + Auth)│
              └──────────┘           └─────────────┘      └────────────┘
```

1. User uploads a resume via the Streamlit frontend (authenticated via Supabase JWT)
2. FastAPI backend extracts text from the PDF/DOCX
3. Groq's LLM parses the raw text into structured data (skills, experience, projects)
4. spaCy + Sentence-BERT run NLP analysis: entity detection, semantic skill validation, JD comparison
5. A weighted scoring engine calculates the final ATS score across 5 components
6. Results are saved to Supabase and returned to the frontend for display and PDF export

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- A [Supabase](https://supabase.com) project (for auth + database)
- A [Groq](https://groq.com) API key

### Installation

```bash
git clone https://github.com/<your-username>/ATS_SCORER.git
cd ATS_SCORER

python -m venv venv
venv\Scripts\Activate.ps1      # Windows
# source venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
python -m spacy download en_core_web_md
```

### Environment Variables

Create a `.env` file in the project root:

```
SUPABASE_URL=
SUPABASE_KEY=
SUPABASE_ANON_KEY=
SUPABASE_JWT_SECRET=
GROQ_API_KEY=
```

### Running the App

Terminal 1 — start the backend:
```bash
python -m backend.main
```

Terminal 2 — start the frontend:
```bash
streamlit run frontend/streamlit_app.py
```

The backend runs on `http://localhost:8000` (docs at `/docs`), and the frontend on `http://localhost:8501`.

## 🐳 Running with Docker

The entire app (backend + frontend) is containerized and available on Docker Hub.

### Pull and run directly

```bash
docker pull priyansh5002/ats-scorer:latest
docker run -p 8000:8000 -p 8501:8501 --env-file .env priyansh5002/ats-scorer:latest
```

### Or build locally

```bash
docker build -t ats-scorer .
docker run -p 8000:8000 -p 8501:8501 --env-file .env ats-scorer
```

The app will be available at `http://localhost:8501` (frontend) and `http://localhost:8000/docs` (backend API docs).

> Note: you'll need a `.env` file with your Supabase and Groq credentials (see [Environment Variables](#environment-variables) above) for the container to function.

## 📊 Scoring Breakdown

| Component | Weight | What it Measures |
|---|---|---|
| Formatting | 20 pts | Section structure, bullet points, completeness |
| Keywords & Skills | 25 pts | Keyword density, relevance, JD keyword match |
| Content Quality | 25 pts | Action verbs, quantifiable achievements, grammar |
| Skill Validation | 15 pts | % of skills backed by project/experience evidence |
| ATS Compatibility | 15 pts | Privacy risks, parsing blockers, clean structure |

## 📄 License

This project is for educational/portfolio purposes.
