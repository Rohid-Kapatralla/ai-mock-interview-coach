from flask import Flask, render_template, request, send_file, session
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth
import fitz
import os
from datetime import datetime


# =========================================================
# FLASK APPLICATION
# =========================================================

app = Flask(__name__)

app.secret_key = os.environ["SECRET_KEY"]


# =========================================================
# UPLOAD FOLDER
# =========================================================

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# =========================================================
# SKILLS DATABASE
# =========================================================

SKILLS_DB = [
    "Python",
    "Java",
    "HTML",
    "CSS",
    "JavaScript",
    "SQL",
    "MySQL",
    "Flask",
    "Git",
    "GitHub",
    "Machine Learning",
    "Artificial Intelligence"
]


# =========================================================
# EXTRACT SKILLS FROM RESUME
# =========================================================

def extract_skills(resume_text):

    skills_found = []

    resume_lower = resume_text.lower()

    for skill in SKILLS_DB:

        if skill.lower() in resume_lower:
            skills_found.append(skill)

    return skills_found


# =========================================================
# GENERATE INTERVIEW QUESTIONS
# =========================================================

def generate_questions(interview_type, skills, job_role):

    questions = []

    interview_type_lower = interview_type.strip().lower()


    # =====================================================
    # TECHNICAL INTERVIEW
    # =====================================================

    if interview_type_lower in [
        "technical",
        "technical interview"
    ]:

        if "Python" in skills:

            questions.append(
                "Explain your experience with Python and mention one project where you used it."
            )

        if "Java" in skills:

            questions.append(
                "What are the main features of Java and why is it widely used?"
            )

        if "HTML" in skills:

            questions.append(
                "What is the difference between HTML and HTML5?"
            )

        if "CSS" in skills:

            questions.append(
                "Explain the CSS Box Model with an example."
            )

        if "JavaScript" in skills:

            questions.append(
                "Explain the difference between var, let and const in JavaScript."
            )

        if "Flask" in skills:

            questions.append(
                "Explain how you used Flask in one of your projects."
            )

        if "SQL" in skills or "MySQL" in skills:

            questions.append(
                "What is the difference between SQL and MySQL?"
            )

        if "Machine Learning" in skills:

            questions.append(
                "Explain one Machine Learning concept or project you know."
            )

        if "Artificial Intelligence" in skills:

            questions.append(
                "What is Artificial Intelligence and how can it be used in software applications?"
            )

        questions.append(
            f"Why are you interested in the {job_role} role?"
        )

        questions.append(
            "Explain one important project from your resume."
        )

        questions.append(
            "What technical skills do you want to improve?"
        )


    # =====================================================
    # BEHAVIORAL INTERVIEW
    # =====================================================

    elif interview_type_lower in [
        "behavioral",
        "behavioral interview"
    ]:

        questions = [

            "Tell me about yourself.",

            "Describe a difficult situation and how you handled it.",

            "How do you manage deadlines and pressure?",

            "Tell me about a teamwork experience.",

            "Describe a mistake you made and what you learned from it."

        ]


    # =====================================================
    # HR INTERVIEW
    # =====================================================

    else:

        questions = [

            "Tell me about yourself.",

            "Why should we hire you?",

            "What are your strengths and weaknesses?",

            f"Why do you want to work as a {job_role}?",

            "Where do you see yourself in five years?"

        ]


    # =====================================================
    # DEFAULT QUESTIONS
    # =====================================================

    default_questions = [

        "Tell me about yourself.",

        "Why should we hire you?",

        "Explain one of your projects.",

        "What are your strengths?",

        "Where do you see yourself in five years?"

    ]


    for question in default_questions:

        if len(questions) >= 5:
            break

        if question not in questions:
            questions.append(question)


    return questions[:5]


# =========================================================
# PERFORMANCE-BASED ANSWER EVALUATION
# =========================================================

def evaluate_answers(answers):

    communication = 0
    technical = 0
    confidence = 0
    relevance = 0


    # =====================================================
    # TECHNICAL TERMS
    # =====================================================

    technical_words = [

        "python",
        "java",
        "html",
        "css",
        "javascript",
        "sql",
        "mysql",
        "flask",
        "machine learning",
        "artificial intelligence",
        "database",
        "api",
        "programming",
        "algorithm",
        "function",
        "class",
        "object",
        "framework",
        "backend",
        "frontend",
        "development",
        "software",
        "project",
        "testing",
        "debugging",
        "server",
        "application",
        "code",
        "coding",
        "data",
        "model",
        "web"
    ]


    # =====================================================
    # EXPERIENCE / CONFIDENCE TERMS
    # =====================================================

    experience_words = [

        "developed",
        "created",
        "implemented",
        "built",
        "designed",
        "managed",
        "improved",
        "achieved",
        "solved",
        "worked",
        "learned",
        "experience",
        "responsible",
        "successfully",
        "completed",
        "contributed",
        "handled",
        "participated",
        "used",
        "project",
        "application",
        "team",
        "my",
        "i"

    ]


    # =====================================================
    # EXPLANATION TERMS
    # =====================================================

    explanation_words = [

        "because",
        "therefore",
        "example",
        "such as",
        "reason",
        "experience",
        "result",
        "solution",
        "approach",
        "learned",
        "problem",
        "process",
        "benefit",
        "difference",
        "used",
        "first",
        "second",
        "finally",
        "however",
        "which",
        "where",
        "when",
        "how",
        "why"

    ]


    # =====================================================
    # EVALUATE EACH ANSWER
    # =====================================================

    for answer in answers:

        text = answer.strip().lower()

        words = text.split()

        word_count = len(words)


        # =================================================
        # EMPTY ANSWER
        # =================================================

        if word_count == 0:

            continue


        # =================================================
        # COMMUNICATION SCORE
        # =================================================

        if word_count >= 60:

            communication += 20

        elif word_count >= 45:

            communication += 18

        elif word_count >= 35:

            communication += 17

        elif word_count >= 25:

            communication += 15

        elif word_count >= 18:

            communication += 13

        elif word_count >= 12:

            communication += 10

        elif word_count >= 7:

            communication += 7

        elif word_count >= 3:

            communication += 4

        else:

            communication += 2


        # =================================================
        # TECHNICAL KNOWLEDGE SCORE
        # =================================================

        technical_matches = 0

        for term in technical_words:

            if term in text:

                technical_matches += 1


        if technical_matches >= 5:

            technical += 20

        elif technical_matches == 4:

            technical += 17

        elif technical_matches == 3:

            technical += 14

        elif technical_matches == 2:

            technical += 10

        elif technical_matches == 1:

            technical += 6

        else:

            if word_count >= 15:

                technical += 5

            else:

                technical += 2


        # =================================================
        # CONFIDENCE SCORE
        # =================================================

        confidence_matches = 0

        for term in experience_words:

            if term in text:

                confidence_matches += 1


        if confidence_matches >= 4:

            confidence += 20

        elif confidence_matches == 3:

            confidence += 17

        elif confidence_matches == 2:

            confidence += 14

        elif confidence_matches == 1:

            confidence += 10

        else:

            if word_count >= 40:

                confidence += 12

            elif word_count >= 25:

                confidence += 9

            elif word_count >= 15:

                confidence += 7

            elif word_count >= 8:

                confidence += 4

            else:

                confidence += 2


        # =================================================
        # ANSWER QUALITY
        # =================================================

        explanation_matches = 0

        for term in explanation_words:

            if term in text:

                explanation_matches += 1


        quality_score = 0


        if word_count >= 50:

            quality_score += 10

        elif word_count >= 35:

            quality_score += 9

        elif word_count >= 25:

            quality_score += 8

        elif word_count >= 15:

            quality_score += 6

        elif word_count >= 8:

            quality_score += 4

        else:

            quality_score += 2


        quality_score += min(

            10,

            explanation_matches * 2

        )


        relevance += min(

            20,

            quality_score

        )


    # =====================================================
    # LIMIT SCORES
    # =====================================================

    communication = min(100, communication)

    technical = min(100, technical)

    confidence = min(100, confidence)

    relevance = min(100, relevance)


    # =====================================================
    # OVERALL SCORE
    # =====================================================

    overall = int(

        communication * 0.35

        + technical * 0.35

        + confidence * 0.15

        + relevance * 0.15

    )


    # =====================================================
    # PERFORMANCE LEVEL
    # =====================================================

    if overall >= 85:

        performance = "Excellent Performance"

    elif overall >= 70:

        performance = "Very Good Performance"

    elif overall >= 55:

        performance = "Good Performance"

    elif overall >= 40:

        performance = "Average Performance"

    else:

        performance = "Needs Improvement"


    # =====================================================
    # DYNAMIC STRENGTHS
    # =====================================================

    strengths = []

    improvements = []


    # Communication

    if communication >= 80:

        strengths.append(
            "Excellent communication with detailed and well-structured responses."
        )

    elif communication >= 70:

        strengths.append(
            "Strong communication and detailed answers."
        )

    elif communication >= 55:

        strengths.append(
            "Reasonable communication with clear basic responses."
        )

    else:

        improvements.append(
            "Give longer and more structured answers."
        )


    # Technical

    if technical >= 80:

        strengths.append(
            "Strong technical knowledge with relevant technical concepts."
        )

    elif technical >= 70:

        strengths.append(
            "Good understanding of technical concepts."
        )

    elif technical >= 55:

        strengths.append(
            "Shows a basic understanding of technical concepts."
        )

    else:

        improvements.append(
            "Include more technical concepts and practical examples."
        )


    # Confidence

    if confidence >= 80:

        strengths.append(
            "Demonstrates strong confidence and practical experience."
        )

    elif confidence >= 70:

        strengths.append(
            "Answers demonstrate confidence and practical experience."
        )

    elif confidence >= 55:

        strengths.append(
            "Shows some practical experience and confidence."
        )

    else:

        improvements.append(
            "Use confident language and explain your experience clearly."
        )


    # Answer Quality

    if relevance >= 80:

        strengths.append(
            "Answers are detailed, relevant and supported with explanations."
        )

    elif relevance >= 70:

        strengths.append(
            "Answers include useful explanations and examples."
        )

    elif relevance >= 55:

        strengths.append(
            "Answers contain some explanation and supporting details."
        )

    else:

        improvements.append(
            "Explain your reasoning and provide examples where possible."
        )


    # =====================================================
    # FALLBACK
    # =====================================================

    if not strengths:

        strengths.append(
            "Completed the interview and attempted all questions."
        )


    if not improvements:

        improvements.append(
            "Continue practicing mock interviews to improve consistency."
        )


    # =====================================================
    # RETURN REPORT
    # =====================================================

    return {

        "overall": overall,

        "communication": communication,

        "technical": technical,

        "confidence": confidence,

        "relevance": relevance,

        "performance": performance,

        "strengths": strengths,

        "improvements": improvements

    }


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def home():

    return render_template("index.html")


# =========================================================
# UPLOAD PAGE
# =========================================================

@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        file = request.files.get("resume")

        interview_type = request.form.get(
            "interview_type",
            "Technical Interview"
        )

        job_role = request.form.get(
            "job_role",
            "Software Engineer"
        )


        # -------------------------------------------------
        # CHECK FILE
        # -------------------------------------------------

        if not file or file.filename == "":

            return "Please upload a resume PDF."


        # -------------------------------------------------
        # SAVE INTERVIEW DETAILS
        # -------------------------------------------------

        session["job_role"] = job_role

        session["interview_type"] = interview_type


        # -------------------------------------------------
        # SAVE RESUME
        # -------------------------------------------------

        filepath = os.path.join(

            app.config["UPLOAD_FOLDER"],

            file.filename

        )

        file.save(filepath)


        # -------------------------------------------------
        # READ RESUME
        # -------------------------------------------------

        doc = fitz.open(filepath)

        resume_text = ""


        for page in doc:

            resume_text += page.get_text()


        doc.close()


        # -------------------------------------------------
        # EXTRACT SKILLS
        # -------------------------------------------------

        skills = extract_skills(resume_text)


        # -------------------------------------------------
        # GENERATE QUESTIONS
        # -------------------------------------------------

        questions = generate_questions(

            interview_type,

            skills,

            job_role

        )


        # -------------------------------------------------
        # SHOW INTERVIEW
        # -------------------------------------------------

        return render_template(

            "interview.html",

            questions=questions,

            resume_text=resume_text,

            interview_type=interview_type,

            job_role=job_role,

            skills=skills

        )


    return render_template("upload.html")


# =========================================================
# RESULT PAGE
# =========================================================

@app.route("/result", methods=["POST"])
def result():

    answers = []


    # -----------------------------------------------------
    # GET ANSWERS
    # -----------------------------------------------------

    for i in range(1, 6):

        answer = request.form.get(

            f"q{i}",

            ""

        )

        answers.append(answer)


    # -----------------------------------------------------
    # EVALUATE
    # -----------------------------------------------------

    report = evaluate_answers(answers)


    # -----------------------------------------------------
    # GET INTERVIEW DETAILS
    # -----------------------------------------------------

    job_role = session.get(

        "job_role",

        request.form.get(

            "job_role",

            "Software Engineer"

        )

    )


    interview_type = session.get(

        "interview_type",

        request.form.get(

            "interview_type",

            "Technical Interview"

        )

    )


    # -----------------------------------------------------
    # SAVE REPORT
    # -----------------------------------------------------

    session["report"] = report

    session["job_role"] = job_role

    session["interview_type"] = interview_type


    # -----------------------------------------------------
    # RESULT PAGE
    # -----------------------------------------------------

    return render_template(

        "result.html",

        score=report["overall"],

        communication=report["communication"],

        technical=report["technical"],

        confidence=report["confidence"],

        relevance=report["relevance"],

        performance=report["performance"],

        strengths=report["strengths"],

        improvements=report["improvements"]

    )


# =========================================================
# PDF HELPER - SCORE BAR
# =========================================================

def draw_score_bar(c, x, y, width, height, score):

    # Background

    c.setFillColor(

        colors.HexColor("#E5E7EB")

    )

    c.roundRect(

        x,
        y,
        width,
        height,
        5,
        fill=1,
        stroke=0

    )


    # Score fill

    fill_width = width * (score / 100)


    if score >= 80:

        bar_color = colors.HexColor("#16A34A")

    elif score >= 60:

        bar_color = colors.HexColor("#2563EB")

    elif score >= 40:

        bar_color = colors.HexColor("#F59E0B")

    else:

        bar_color = colors.HexColor("#DC2626")


    c.setFillColor(bar_color)


    if fill_width > 0:

        c.roundRect(

            x,
            y,
            fill_width,
            height,
            5,
            fill=1,
            stroke=0

        )


# =========================================================
# PDF HELPER - WRAPPED TEXT
# =========================================================

def draw_wrapped_text(
    c,
    text,
    x,
    y,
    max_width,
    font="Helvetica",
    size=10,
    line_height=15
):

    c.setFont(

        font,

        size

    )


    words = text.split()

    line = ""

    lines = []


    for word in words:

        test_line = (

            line + " " + word

            if line

            else word

        )


        if stringWidth(

            test_line,

            font,

            size

        ) <= max_width:

            line = test_line

        else:

            if line:

                lines.append(line)

            line = word


    if line:

        lines.append(line)


    for current_line in lines:

        c.drawString(

            x,

            y,

            current_line

        )

        y -= line_height


    return y


# =========================================================
# DOWNLOAD PROFESSIONAL PDF REPORT
# =========================================================

@app.route("/download_report")
def download_report():

    report = session.get("report")


    # -----------------------------------------------------
    # CHECK REPORT
    # -----------------------------------------------------

    if not report:

        return (

            "No interview report available. "

            "Please complete an interview first."

        ), 400


    job_role = session.get(

        "job_role",

        "Software Engineer"

    )


    interview_type = session.get(

        "interview_type",

        "Technical Interview"

    )


    # -----------------------------------------------------
    # PDF FILE
    # -----------------------------------------------------

    pdf_file = "Interview_Report.pdf"


    c = canvas.Canvas(

        pdf_file,

        pagesize=letter

    )


    width, height = letter


    # =====================================================
    # BACKGROUND
    # =====================================================

    c.setFillColor(

        colors.HexColor("#F7F9FC")

    )


    c.rect(

        0,
        0,
        width,
        height,
        fill=1,
        stroke=0

    )


    # =====================================================
    # HEADER
    # =====================================================

    c.setFillColor(

        colors.HexColor("#1E3A8A")

    )


    c.rect(

        0,
        height - 95,
        width,
        95,
        fill=1,
        stroke=0

    )


    c.setFillColor(colors.white)


    c.setFont(

        "Helvetica-Bold",

        23

    )


    c.drawString(

        40,

        height - 45,

        "AI MOCK INTERVIEW COACH"

    )


    c.setFont(

        "Helvetica",

        11

    )


    c.drawString(

        42,

        height - 68,

        "Professional Interview Performance Report"

    )


    generated_date = datetime.now().strftime(

        "%d-%m-%Y  %I:%M %p"

    )


    c.drawRightString(

        width - 40,

        height - 68,

        generated_date

    )


    # =====================================================
    # INTERVIEW DETAILS
    # =====================================================

    card_y = height - 190


    c.setFillColor(colors.white)


    c.roundRect(

        40,
        card_y,
        width - 80,
        70,
        10,
        fill=1,
        stroke=0

    )


    c.setFillColor(

        colors.HexColor("#111827")

    )


    c.setFont(

        "Helvetica-Bold",

        14

    )


    c.drawString(

        55,

        card_y + 45,

        "Interview Details"

    )


    c.setFont(

        "Helvetica",

        11

    )


    c.drawString(

        55,

        card_y + 22,

        "Job Role: " + str(job_role)

    )


    c.drawString(

        300,

        card_y + 22,

        "Interview Type: " + str(interview_type)

    )


    # =====================================================
    # OVERALL PERFORMANCE
    # =====================================================

    score_card_y = height - 335


    c.setFillColor(colors.white)


    c.roundRect(

        40,
        score_card_y,
        width - 80,
        120,
        10,
        fill=1,
        stroke=0

    )


    c.setFillColor(

        colors.HexColor("#111827")

    )


    c.setFont(

        "Helvetica-Bold",

        15

    )


    c.drawString(

        55,

        score_card_y + 88,

        "Overall Performance"

    )


    # Overall score color

    overall_score = report["overall"]


    if overall_score >= 80:

        score_color = "#16A34A"

    elif overall_score >= 60:

        score_color = "#2563EB"

    elif overall_score >= 40:

        score_color = "#F59E0B"

    else:

        score_color = "#DC2626"


    c.setFillColor(

        colors.HexColor(score_color)

    )


    c.setFont(

        "Helvetica-Bold",

        32

    )


    c.drawString(

        55,

        score_card_y + 43,

        str(overall_score) + " / 100"

    )


    c.setFillColor(

        colors.HexColor("#374151")

    )


    c.setFont(

        "Helvetica-Bold",

        12

    )


    c.drawString(

        210,

        score_card_y + 60,

        report["performance"]

    )


    # =====================================================
    # PERFORMANCE BREAKDOWN
    # =====================================================

    breakdown_y = height - 490


    c.setFillColor(colors.white)


    c.roundRect(

        40,
        breakdown_y,
        width - 80,
        135,
        10,
        fill=1,
        stroke=0

    )


    c.setFillColor(

        colors.HexColor("#111827")

    )


    c.setFont(

        "Helvetica-Bold",

        15

    )


    c.drawString(

        55,

        breakdown_y + 108,

        "Performance Breakdown"

    )


    categories = [

        (
            "Communication",
            report["communication"]
        ),

        (
            "Technical Knowledge",
            report["technical"]
        ),

        (
            "Confidence",
            report["confidence"]
        ),

        (
            "Answer Quality",
            report["relevance"]
        )

    ]


    bar_x = 190

    bar_width = 270

    row_y = breakdown_y + 78


    for name, score in categories:

        c.setFillColor(

            colors.HexColor("#374151")

        )


        c.setFont(

            "Helvetica",

            10

        )


        c.drawString(

            55,

            row_y + 2,

            name

        )


        draw_score_bar(

            c,

            bar_x,

            row_y,

            bar_width,

            10,

            score

        )


        c.setFillColor(

            colors.HexColor("#111827")

        )


        c.setFont(

            "Helvetica-Bold",

            10

        )


        c.drawString(

            bar_x + bar_width + 12,

            row_y + 1,

            str(score) + "/100"

        )


        row_y -= 27


    # =====================================================
    # STRENGTHS
    # =====================================================

    strengths_y = breakdown_y - 30


    c.setFillColor(colors.white)


    c.roundRect(

        40,
        strengths_y - 105,
        width - 80,
        105,
        10,
        fill=1,
        stroke=0

    )


    c.setFillColor(

        colors.HexColor("#111827")

    )


    c.setFont(

        "Helvetica-Bold",

        15

    )


    c.drawString(

        55,

        strengths_y - 25,

        "Strengths"

    )


    y = strengths_y - 48


    for item in report["strengths"]:

        c.setFillColor(

            colors.HexColor("#16A34A")

        )


        c.drawString(

            58,

            y,

            "+"

        )


        c.setFillColor(

            colors.HexColor("#374151")

        )


        y = draw_wrapped_text(

            c,

            item,

            75,

            y,

            width - 130,

            "Helvetica",

            10,

            14

        )


    # =====================================================
    # AREAS TO IMPROVE
    # =====================================================

    improve_y = strengths_y - 130


    c.setFillColor(colors.white)


    c.roundRect(

        40,
        improve_y - 120,
        width - 80,
        120,
        10,
        fill=1,
        stroke=0

    )


    c.setFillColor(

        colors.HexColor("#111827")

    )


    c.setFont(

        "Helvetica-Bold",

        15

    )


    c.drawString(

        55,

        improve_y - 25,

        "Areas to Improve"

    )


    y = improve_y - 48


    for item in report["improvements"]:

        c.setFillColor(

            colors.HexColor("#DC2626")

        )


        c.drawString(

            58,

            y,

            "-"

        )


        c.setFillColor(

            colors.HexColor("#374151")

        )


        y = draw_wrapped_text(

            c,

            item,

            75,

            y,

            width - 130,

            "Helvetica",

            10,

            14

        )


    # =====================================================
    # FINAL ASSESSMENT
    # =====================================================

    feedback_y = improve_y - 145


    c.setFillColor(colors.white)


    c.roundRect(

        40,
        feedback_y - 105,
        width - 80,
        105,
        10,
        fill=1,
        stroke=0

    )


    c.setFillColor(

        colors.HexColor("#111827")

    )


    c.setFont(

        "Helvetica-Bold",

        15

    )


    c.drawString(

        55,

        feedback_y - 25,

        "Final Assessment"

    )


    # -----------------------------------------------------
    # DYNAMIC FINAL FEEDBACK
    # -----------------------------------------------------

    if overall_score >= 85:

        feedback = (

            "Excellent performance. The candidate demonstrated "

            "strong communication, technical knowledge, confidence "

            "and high-quality interview responses."

        )

    elif overall_score >= 70:

        feedback = (

            "Very good performance. The candidate demonstrated "

            "good interview skills and a solid technical foundation. "

            "A small amount of additional practice can further "

            "improve performance."

        )

    elif overall_score >= 55:

        feedback = (

            "Good performance. The candidate demonstrated a "

            "reasonable foundation. More practice with technical "

            "explanations and structured answers can improve "

            "interview performance."

        )

    elif overall_score >= 40:

        feedback = (

            "Average performance. The candidate should focus on "

            "giving detailed answers, using relevant examples, "

            "improving technical explanations and speaking with "

            "greater confidence."

        )

    else:

        feedback = (

            "The candidate needs more interview practice. Focus "

            "on communication, technical concepts, answer quality "

            "and confidence before attending real interviews."

        )


    draw_wrapped_text(

        c,

        feedback,

        55,

        feedback_y - 50,

        width - 110,

        "Helvetica",

        10,

        15

    )


    # =====================================================
    # FOOTER
    # =====================================================

    c.setFillColor(

        colors.HexColor("#6B7280")

    )


    c.setFont(

        "Helvetica",

        8

    )


    c.drawCentredString(

        width / 2,

        20,

        "AI Mock Interview Coach | Performance Evaluation Report"

    )


    # =====================================================
    # SAVE PDF
    # =====================================================

    c.save()


    # =====================================================
    # SEND PDF
    # =====================================================

    return send_file(

        pdf_file,

        as_attachment=True,

        download_name="AI_Mock_Interview_Report.pdf"

    )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(debug=os.environ.get("FLASK_DEBUG", "0") == "1")
