# AI Mock Interview Coach

A Flask-based mock interview practice application that:
- Accepts a candidate resume in PDF format
- Extracts skills from the resume
- Generates interview questions based on interview type, role, and detected skills
- Evaluates submitted answers across communication, technical knowledge, confidence, and answer quality
- Generates a downloadable interview performance report as a PDF

## Tech Stack

- Python 3.13
- Flask
- PyMuPDF
- ReportLab
- HTML / CSS
- Gunicorn (production server)

## Run locally

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
# source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file locally if you want to set a secret key:

```text
SECRET_KEY=replace-with-a-random-secret
```

Then run:

```bash
python app.py
```

Open `http://127.0.0.1:5000`.

## Deploy on Render

Use a Render **Web Service** connected to this GitHub repository.

- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- Python version: provided by `.python-version`
- Environment variable: `SECRET_KEY` = a strong random secret

Do not commit `.env`, API keys, uploaded resumes, virtual environments, or generated reports.

## Project structure

```text
AI_Mock_Interview_Coach/
├── app.py
├── requirements.txt
├── .gitignore
├── .python-version
├── templates/
│   ├── index.html
│   ├── interview.html
│   ├── result.html
│   └── upload.html
├── static/
│   └── style.css
└── uploads/
    └── .gitkeep
```

## Note

The current implementation uses a rule-based question generation and answer-scoring system. It does not currently call the Gemini API, even though the original project folder contained a `GEMINI_API_KEY` environment variable. If the project is presented as a Generative AI application, the Gemini integration should be added and tested before making that claim.
