# """
# Shubham Burman - Portfolio AI Backend Service
# FastAPI REST API providing profile metadata, AI conversational endpoint, and contact handling.
# """

# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel, EmailStr
# from typing import Optional, List
# import datetime

# app = FastAPI(
#     title=" Shubham Kumar Burman Portfolio AI API",
#     description="Backend API powering Shubham Burman's AI Portfolio and Recruiter Assistant",
#     version="1.0.0"
# )

# # Enable CORS for frontend integration
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Profile data matching Rakesh's Resume
# PROFILE_DATA = {
#     "name": "Shubham Burman",
#     "title": "Aspiring Full Stack Developer",
#     "specialization": "Full Stack Web Development (MERN Stack)",
#     "location": "Asansol, West Bengal, India",
#     "contact": {
#         "email": "shubhamkumarburman07@gmail.com",
#         "phone": "+91-6294846716",
#         "github": "https://github.com",
#         "linkedin": "https://linkedin.com"
#     },
#     "education": {
#         "degree": "B.Tech in Computer Science & Engineering (Information Technology)",
#           "stream": "Information Technology",
#         "institution": "JIS College of Engineering, Kalyani",
#         "duration": "2023 – 2027",
#         "cgpa": "7.30 / 10 (through 6th Semester)"
#     },
#   "skills": {
#         "programming": ["Python", "Java", "C", "JavaScript", "SQL"],
#         "frontend": ["HTML", "CSS", "Tailwind CSS", "React.js"],
#         "backend": ["Node.js", "Express.js", "REST APIs", "JWT"],
#         "database": ["MongoDB", "Mongoose"],
#         "ai_ml": ["Machine Learning", "NLP", "Generative AI", "Google Gemini AI"],
#         "data_science": ["Scikit-learn", "NLTK", "Matplotlib", "TF-IDF"],
#         "tools": ["Git", "GitHub", "VS Code", "Postman"]
#     },
#     "projects": [
#         {
#             "id": "aiinterview",
#             "name": "AI Interview Agent",
#             "tech": "React.js, Node.js, Express.js, MongoDB, Multi-Agent LLMs",
#             "summary": "AI-powered interview agent that conducts, analyzes and evaluates technical interviews in real-time with intelligent feedback and performance insights."
#         },
#         {
#             "id": "aischoolhouse",
#             "name": "The AI Schoolhouse",
#             "tech": "React.js, Tailwind CSS, Node.js, Express.js, MongoDB, JWT, Google Gemini AI",
#             "summary": "AI-powered learning platform where students upload PDF/DOCX/TXT textbooks to get AI summaries, ask textbook-based questions, take quizzes, create flashcards and track study progress."
#         },
#         {
#             "id": "resumeanalyzer",
#             "name": "AI Resume Analyzer",
#             "tech": "Python, Machine Learning, NLTK, scikit-learn, TF-IDF, Google Gemini AI",
#             "summary": "NLP-based system that matches resumes against job descriptions using TF-IDF and Cosine Similarity, detects missing skills and generates improvement suggestions."
#         },
#         {
#             "id": "razorpayclone",
#             "name": "Razorpay Clone",
#             "tech": "HTML, Tailwind CSS",
#             "summary": "Responsive frontend replica of the Razorpay landing page with modern UI components."
#         }
#     ],
#     "certifications": [
#         {
#             "title": "NPTEL - Programming in Java",
#             "organization": "IIT Kharagpur",
#             "year": 2025
#         },
#         {
#             "title": "NPTEL - E-Business",
#             "organization": "IIT Kharagpur",
#             "year": 2025
#         },
#         {
#             "title": "NPTEL - Introduction to Machine Learning",
#             "organization": "IIT Madras",
#             "year": 2026
#         },
#         {
#             "title": "AI-ML Virtual Internship",
#             "organization": "EduSkills Foundation",
#             "year": 2026
#         },
#         {
#             "title": "Python Full Stack Developer Virtual Internship",
#             "organization": "EduSkills Foundation",
#             "year": 2026
#         },
#         {
#             "title": "Mobile App Development with React Native",
#             "organization": "EduSkills Academy",
#             "year": 2026
#         },
#         {
#             "title": "Java Full Stack Development with Project Virtual Internship",
#             "organization": "EduSkills Academy",
#             "year": 2026
#         },
#         {
#             "title": "Android Developer Virtual Internship",
#             "organization": "EduSkills Foundation",
#             "year": 2026
#         },
#         {
#             "title": "Full Stack Development (MERN) Training - Grade A",
#             "organization": "Ardent Computech Pvt. Ltd. (JIS College of Engineering)",
#             "year": 2026
#         }
#     ],
#     "career_target": {
#         "role": "Full Stack Developer — Fresher / Junior",
#         "focus": ["React.js", "Node.js", "Express.js", "MongoDB", "Tailwind CSS", "REST APIs", "Python", "Generative AI"]
#     }
# }

# class ChatQuery(BaseModel):
#     query: str

# class ChatResponse(BaseModel):
#     query: str
#     response: str
#     timestamp: str

# class ContactMessage(BaseModel):
#     name: str
#     email: str
#     message: str

# @app.get("/")
# def home():
#     return {
#         "status": "online",
#         "message": "Welcome to Rakesh Pal's AI Portfolio Backend API!",
#         "docs_url": "/docs"
#     }

# @app.get("/health")
# def health():
#     return {"status": "healthy", "service": "fastapi-ai-backend"}

# @app.get("/api/profile")
# def get_profile():
#     """Returns full structured profile data of Rakesh Pal."""
#     return PROFILE_DATA

# @app.post("/api/chat", response_model=ChatResponse)
# def chat_ai(query_data: ChatQuery):
#     """
#     Intelligent endpoint processing recruiter and visitor questions.
#     """
#     q = query_data.query.lower().strip()
    
#     if any(k in q for k in ["who", "about", "rakesh", "bio"]):
#         reply = (
#             f"{PROFILE_DATA['name']} is a passionate {PROFILE_DATA['title']} studying "
#             f"{PROFILE_DATA['education']['degree']} ({PROFILE_DATA['education']['stream']}) "
#             f"at {PROFILE_DATA['education']['institution']} with an impressive CGPA of "
#             f"{PROFILE_DATA['education']['cgpa']}."
#         )
#     elif any(k in q for k in ["skill", "tech", "python", "fastapi", "stack", "machine learning"]):
#         all_skills = ", ".join(
#             PROFILE_DATA['skills']['programming'] + 
#             PROFILE_DATA['skills']['ai_ml'] + 
#             PROFILE_DATA['skills']['backend']
#         )
#         reply = f"Rakesh specializes in: {all_skills}. He builds production-ready FastAPI backends and applied AI systems."
#     elif any(k in q for k in ["project", "chatbot", "face", "game", "tic tac"]):
#         project_titles = [f"{p['name']} ({p['tech']})" for p in PROFILE_DATA['projects']]
#         reply = f"Rakesh has engineered standout AI projects including: {'; '.join(project_titles)}."
#     elif any(k in q for k in ["cgpa", "college", "university", "education", "score", "grade"]):
#         reply = (
#             f"Rakesh attends {PROFILE_DATA['education']['institution']} for {PROFILE_DATA['education']['degree']}. "
#             f"His current academic score is {PROFILE_DATA['education']['cgpa']}."
#         )
#     elif any(k in q for k in ["contact", "email", "phone", "reach", "hire", "number"]):
#         reply = (
#             f"You can reach Rakesh via Email: {PROFILE_DATA['contact']['email']} or "
#             f"Phone: {PROFILE_DATA['contact']['phone']}. He is actively interviewing for AI/ML Engineer positions!"
#         )
#     elif any(k in q for k in ["cert", "drone", "fly smart", "achievement"]):
#         cert = PROFILE_DATA['certifications'][0]
#         reply = f"Rakesh participated in {cert['title']} organized by {cert['organization']} ({cert['year']})."
#     else:
#         reply = (
#             f"Rakesh Pal is an AI/ML Engineer skilled in Python, Machine Learning, Computer Vision, and FastAPI. "
#             f"You can check out his projects on the portfolio or email him at {PROFILE_DATA['contact']['email']}."
#         )

#     return ChatResponse(
#         query=query_data.query,
#         response=reply,
#         timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
#     )

# @app.post("/api/contact")
# def submit_contact(msg: ContactMessage):
#     """Receives contact messages from the portfolio website."""
#     return {
#         "status": "received",
#         "message": f"Thank you, {msg.name}! Your message has been noted.",
#         "details": msg.model_dump()
#     }



"""
Shubham Burman - Portfolio AI Backend Service
FastAPI REST API providing profile metadata, AI conversational endpoint, and contact handling.
Contact messages are emailed to the portfolio owner via Gmail SMTP.
"""

import datetime
import os
import re
import smtplib
import ssl
import time
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Load secrets from backend/.env (never commit this file)
load_dotenv(Path(__file__).parent / ".env")

app = FastAPI(
    title="Shubham Kumar Burman Portfolio AI API",
    description="Backend API powering Shubham Burman's AI Portfolio and Recruiter Assistant",
    version="1.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Profile data matching Shubham's Resume
PROFILE_DATA = {
    "name": "Shubham Burman",
    "title": "Aspiring Full Stack Developer",
    "specialization": "Full Stack Web Development (MERN Stack)",
    "location": "Asansol, West Bengal, India",
    "contact": {
        "email": "shubhamkumarburman07@gmail.com",
        "phone": "+91-6294846716",
        "github": "https://github.com/ShubhamKB04",
        "linkedin": "https://linkedin.com"
    },
    "education": {
        "degree": "B.Tech in Computer Science & Engineering (Information Technology)",
        "stream": "Information Technology",
        "institution": "JIS College of Engineering, Kalyani",
        "duration": "2023 – 2027",
        "cgpa": "7.30 / 10 (through 6th Semester)"
    },
    "skills": {
        "programming": ["Python", "Java", "C", "JavaScript", "SQL"],
        "frontend": ["HTML", "CSS", "Tailwind CSS", "React.js"],
        "backend": ["Node.js", "Express.js", "REST APIs", "JWT"],
        "database": ["MongoDB", "Mongoose"],
        "ai_ml": ["Machine Learning", "NLP", "Generative AI", "Google Gemini AI"],
        "data_science": ["Scikit-learn", "NLTK", "Matplotlib", "TF-IDF"],
        "tools": ["Git", "GitHub", "VS Code", "Postman"]
    },
    "projects": [
        {"id": "aiinterview", "name": "AI Interview Agent", "tech": "React.js, Node.js, Express.js, MongoDB, Multi-Agent LLMs",
         "summary": "AI-powered interview agent that conducts, analyzes and evaluates technical interviews in real-time with intelligent feedback and performance insights."},
        {"id": "aischoolhouse", "name": "The AI Schoolhouse", "tech": "React.js, Tailwind CSS, Node.js, Express.js, MongoDB, JWT, Google Gemini AI",
         "summary": "AI-powered learning platform where students upload PDF/DOCX/TXT textbooks to get AI summaries, ask textbook-based questions, take quizzes, create flashcards and track study progress."},
        {"id": "resumeanalyzer", "name": "AI Resume Analyzer", "tech": "Python, Machine Learning, NLTK, scikit-learn, TF-IDF, Google Gemini AI",
         "summary": "NLP-based system that matches resumes against job descriptions using TF-IDF and Cosine Similarity, detects missing skills and generates improvement suggestions."},
        {"id": "razorpayclone", "name": "Razorpay Clone", "tech": "HTML, Tailwind CSS",
         "summary": "Responsive frontend replica of the Razorpay landing page with modern UI components."}
    ],
    "certifications": [
        {"title": "NPTEL - Programming in Java", "organization": "IIT Kharagpur", "year": 2025},
        {"title": "NPTEL - E-Business", "organization": "IIT Kharagpur", "year": 2025},
        {"title": "NPTEL - Introduction to Machine Learning", "organization": "IIT Madras", "year": 2026},
        {"title": "AI-ML Virtual Internship", "organization": "EduSkills Foundation", "year": 2026},
        {"title": "Python Full Stack Developer Virtual Internship", "organization": "EduSkills Foundation", "year": 2026},
        {"title": "Mobile App Development with React Native", "organization": "EduSkills Academy", "year": 2026},
        {"title": "Java Full Stack Development with Project Virtual Internship", "organization": "EduSkills Academy", "year": 2026},
        {"title": "Android Developer Virtual Internship", "organization": "EduSkills Foundation", "year": 2026},
        {"title": "Full Stack Development (MERN) Training - Grade A", "organization": "Ardent Computech Pvt. Ltd. (JIS College of Engineering)", "year": 2026}
    ],
    "career_target": {
        "role": "Full Stack Developer — Fresher / Junior",
        "focus": ["React.js", "Node.js", "Express.js", "MongoDB", "Tailwind CSS", "REST APIs", "Python", "Generative AI"]
    }
}


class ChatQuery(BaseModel):
    query: str


class ChatResponse(BaseModel):
    query: str
    response: str
    timestamp: str


class ContactMessage(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: str = Field(min_length=3, max_length=254)
    message: str = Field(min_length=1, max_length=2000)


# ---------------------------------------------------------------------------
# Contact form: email delivery
# ---------------------------------------------------------------------------
EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
RATE_LIMIT = 5          # max messages per IP
RATE_WINDOW = 3600      # per hour (seconds)
_hits = {}


def _allowed(ip: str) -> bool:
    """Simple in-memory spam protection: max RATE_LIMIT messages per IP per hour."""
    now = time.time()
    recent = [t for t in _hits.get(ip, []) if now - t < RATE_WINDOW]
    if len(recent) >= RATE_LIMIT:
        _hits[ip] = recent
        return False
    recent.append(now)
    _hits[ip] = recent
    return True


def _clean_line(value: str) -> str:
    """Remove line breaks so visitor input can never inject email headers."""
    return re.sub(r"[\r\n]+", " ", value).strip()


def send_contact_email(name: str, sender_email: str, message: str) -> None:
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = (os.getenv("SMTP_APP_PASSWORD") or "").replace(" ", "")
    to_email = os.getenv("CONTACT_TO_EMAIL") or smtp_user

    if not smtp_user or not smtp_password:
        raise RuntimeError("SMTP_USER / SMTP_APP_PASSWORD are not set in backend/.env")

    mail = EmailMessage()
    mail["Subject"] = f"Portfolio message from {name}"
    mail["From"] = formataddr(("Portfolio Contact Form", smtp_user))
    mail["To"] = to_email
    # Reply-To = visitor, so pressing "Reply" in Gmail goes straight to them
    mail["Reply-To"] = formataddr((name, sender_email))
    mail.set_content(
        f"You received a new message from your portfolio website.\n\n"
        f"Name:  {name}\n"
        f"Email: {sender_email}\n\n"
        f"Message:\n{message}\n"
    )

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context, timeout=15) as server:
        server.login(smtp_user, smtp_password)
        server.send_message(mail)


@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Welcome to Shubham Burman's AI Portfolio Backend API!",
        "docs_url": "/docs"
    }


@app.get("/health")
def health():
    return {"status": "healthy", "service": "fastapi-ai-backend"}


@app.get("/api/profile")
def get_profile():
    """Returns full structured profile data of Shubham Burman."""
    return PROFILE_DATA


@app.post("/api/chat", response_model=ChatResponse)
def chat_ai(query_data: ChatQuery):
    """
    Intelligent endpoint processing recruiter and visitor questions.
    """
    q = query_data.query.lower().strip()
    p = PROFILE_DATA

    if any(k in q for k in ["contact", "email", "phone", "reach", "hire", "number"]):
        reply = (
            f"You can reach Shubham via Email: {p['contact']['email']} or Phone: {p['contact']['phone']}. "
            f"He is looking for {p['career_target']['role']} opportunities."
        )
    elif any(k in q for k in ["education", "college", "university", "degree", "study"]):
        reply = (
            f"Shubham is pursuing {p['education']['degree']} at {p['education']['institution']} "
            f"({p['education']['duration']})."
        )
    elif any(k in q for k in ["skill", "tech", "python", "react", "stack", "node", "mongo"]):
        all_skills = ", ".join(
            p["skills"]["programming"] + p["skills"]["frontend"] +
            p["skills"]["backend"] + p["skills"]["database"] + p["skills"]["ai_ml"]
        )
        reply = f"Shubham's skills include: {all_skills}. He builds full-stack MERN apps with AI features."
    elif any(k in q for k in ["project", "schoolhouse", "interview", "resume analyzer", "razorpay"]):
        titles = [f"{x['name']} ({x['tech']})" for x in p["projects"]]
        reply = f"Shubham's projects: {'; '.join(titles)}."
    elif any(k in q for k in ["cert", "internship", "nptel", "achievement", "jistech", "winner"]):
        reply = (
            "Shubham is the winner of JISTech 2K23 (web development project) and holds NPTEL certifications "
            "in Java, E-Business and Machine Learning, plus EduSkills virtual internships and a MERN training with Grade A."
        )
    elif any(k in q for k in ["who", "shubham", "bio", "introduce"]):
        reply = (
            f"{p['name']} is an {p['title']} and B.Tech IT student at {p['education']['institution']}, "
            f"focused on {p['specialization']}."
        )
    else:
        reply = (
            f"{p['name']} is a Full Stack Developer skilled in React, Node.js, Express, MongoDB and Python. "
            f"You can check out his projects on the portfolio or email him at {p['contact']['email']}."
        )

    return ChatResponse(
        query=query_data.query,
        response=reply,
        timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
    )


@app.post("/api/contact")
def submit_contact(msg: ContactMessage, request: Request):
    """Receives contact messages from the portfolio website and emails them to the owner."""
    ip = request.client.host if request.client else "unknown"
    if not _allowed(ip):
        raise HTTPException(status_code=429, detail="Too many messages. Please try again later.")

    name = _clean_line(msg.name)
    sender_email = _clean_line(msg.email)
    message = msg.message.strip()

    if not name or not message:
        raise HTTPException(status_code=422, detail="Name and message are required.")
    if not EMAIL_PATTERN.match(sender_email):
        raise HTTPException(status_code=422, detail="Please enter a valid email address.")

    try:
        send_contact_email(name, sender_email, message)
    except Exception as exc:  # log the real reason on the server, keep the reply generic
        print(f"[contact] email failed: {exc}")
        raise HTTPException(status_code=500, detail="Could not send the message. Please try again later.")

    return {"status": "sent", "message": f"Thank you, {name}! Your message has been sent."}