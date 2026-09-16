# AI Mock Interview Coach

A Flask-based mock interview practice platform that analyzes a candidate's resume, extracts relevant skills, generates personalized interview questions, evaluates answers, and produces a downloadable performance report.

## 🚀 Features

- 📄 Upload and process resume PDFs
- 🔍 Extract candidate skills from resumes
- 🎯 Select interview type and job role
- ❓ Generate interview questions based on the selected role and detected skills
- 📝 Evaluate interview answers
- 📊 Calculate interview performance scores
- 📋 Evaluate communication, technical knowledge, confidence, and answer quality
- 📥 Generate downloadable interview performance reports
- 📱 Responsive and user-friendly web interface
- 🌐 Production-ready Flask application with Gunicorn

## 🛠️ Tech Stack

### Programming Language
- Python 3.13

### Backend
- Flask

### PDF Processing
- PyMuPDF

### PDF Report Generation
- ReportLab

### Frontend
- HTML5
- CSS3
- Jinja2 Templates

### Deployment
- Gunicorn

## 🔄 How It Works

The application follows the following workflow:

1. **Upload Resume**
   - The candidate uploads their resume in PDF format.

2. **Resume Processing**
   - The application extracts text from the uploaded resume using PyMuPDF.

3. **Skill Extraction**
   - Relevant technical and professional skills are identified from the extracted resume content.

4. **Interview Configuration**
   - The candidate selects the interview type and target job role.

5. **Question Generation**
   - Interview questions are generated based on the selected interview type, job role, and detected candidate skills.

6. **Answer Evaluation**
   - Candidate responses are evaluated using the application's scoring logic.

7. **Performance Analysis**
   - The application evaluates areas such as:
     - Communication
     - Technical Knowledge
     - Confidence
     - Answer Quality

8. **Performance Report**
   - A downloadable PDF report is generated using ReportLab.

## 📂 Project Structure

```text
ai-mock-interview-coach/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── ...
│
├── static/
│   ├── css/
│   ├── js/
│   └── ...
│
└── uploads/
    └── .gitkeep
