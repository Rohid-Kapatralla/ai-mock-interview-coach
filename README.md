# AI Mock Interview Coach

A Flask-based mock interview practice platform that analyzes a candidate's resume, identifies relevant skills, generates role-specific interview questions, evaluates answers, and produces a downloadable performance report.

## Features

- Upload candidate resume in PDF format
- Extract skills from uploaded resumes
- Select interview type and target role
- Generate interview questions based on role, interview type, and detected skills
- Evaluate submitted answers
- Analyze communication, technical knowledge, confidence, and answer quality
- Calculate an overall interview performance score
- Generate downloadable interview performance reports in PDF format
- Responsive web interface for interview practice

## Tech Stack

- **Language:** Python 3.13
- **Backend:** Flask
- **PDF Processing:** PyMuPDF
- **PDF Report Generation:** ReportLab
- **Frontend:** HTML5, CSS3
- **Production Server:** Gunicorn

## How It Works

1. Upload a resume in PDF format.
2. The application extracts relevant skills from the resume.
3. Select the interview type and target job role.
4. The system generates interview questions based on the selected role and detected skills.
5. Submit answers to the generated questions.
6. The application evaluates the responses across multiple criteria.
7. Review the interview performance results.
8. Download the generated performance report as a PDF.

## Project Structure

```text
AI_Mock_Interview_Coach/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .python-version
│
├── templates/
│   ├── index.html
│   ├── interview.html
│   ├── result.html
│   └── upload.html
│
├── static/
│   └── style.css
│
└── uploads/
    └── .gitkeep
