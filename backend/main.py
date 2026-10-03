"""
Rakesh Pal - Portfolio AI Backend Service
FastAPI REST API providing profile metadata, AI conversational endpoint, and contact handling.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import Optional, List
import datetime

app = FastAPI(
    title=" Shubham Kumar Burman Portfolio AI API",
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

# Profile data matching Rakesh's Resume
PROFILE_DATA = {
    "name": "Shubham Burman",
    "title": "Aspiring Full Stack Developer",
    "specialization": "Full Stack Web Development (MERN Stack)",
    "location": "Asansol, West Bengal, India",
    "contact": {
        "email": "shubhamkumarburman07@gmail.com",
        "phone": "+91-6294846716",
        "github": "https://github.com",
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
        {
            "id": "aiinterview",
            "name": "AI Interview Agent",
            "tech": "React.js, Node.js, Express.js, MongoDB, Multi-Agent LLMs",
            "summary": "AI-powered interview agent that conducts, analyzes and evaluates technical interviews in real-time with intelligent feedback and performance insights."
        },
        {
            "id": "aischoolhouse",
            "name": "The AI Schoolhouse",
            "tech": "React.js, Tailwind CSS, Node.js, Express.js, MongoDB, JWT, Google Gemini AI",
            "summary": "AI-powered learning platform where students upload PDF/DOCX/TXT textbooks to get AI summaries, ask textbook-based questions, take quizzes, create flashcards and track study progress."
        },
        {
            "id": "resumeanalyzer",
            "name": "AI Resume Analyzer",
            "tech": "Python, Machine Learning, NLTK, scikit-learn, TF-IDF, Google Gemini AI",
            "summary": "NLP-based system that matches resumes against job descriptions using TF-IDF and Cosine Similarity, detects missing skills and generates improvement suggestions."
        },
        {
            "id": "razorpayclone",
            "name": "Razorpay Clone",
            "tech": "HTML, Tailwind CSS",
            "summary": "Responsive frontend replica of the Razorpay landing page with modern UI components."
        }
    ],
    "certifications": [
        {
            "title": "NPTEL - Programming in Java",
            "organization": "IIT Kharagpur",
            "year": 2025
        },
        {
            "title": "NPTEL - E-Business",
            "organization": "IIT Kharagpur",
            "year": 2025
        },
        {
            "title": "NPTEL - Introduction to Machine Learning",
            "organization": "IIT Madras",
            "year": 2026
        },
        {
            "title": "AI-ML Virtual Internship",
            "organization": "EduSkills Foundation",
            "year": 2026
        },
        {
            "title": "Python Full Stack Developer Virtual Internship",
            "organization": "EduSkills Foundation",
            "year": 2026
        },
        {
            "title": "Mobile App Development with React Native",
            "organization": "EduSkills Academy",
            "year": 2026
        },
        {
            "title": "Java Full Stack Development with Project Virtual Internship",
            "organization": "EduSkills Academy",
            "year": 2026
        },
        {
            "title": "Android Developer Virtual Internship",
            "organization": "EduSkills Foundation",
            "year": 2026
        },
        {
            "title": "Full Stack Development (MERN) Training - Grade A",
            "organization": "Ardent Computech Pvt. Ltd. (JIS College of Engineering)",
            "year": 2026
        }
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
    name: str
    email: str
    message: str

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Welcome to Rakesh Pal's AI Portfolio Backend API!",
        "docs_url": "/docs"
    }

@app.get("/health")
def health():
    return {"status": "healthy", "service": "fastapi-ai-backend"}

@app.get("/api/profile")
def get_profile():
    """Returns full structured profile data of Rakesh Pal."""
    return PROFILE_DATA

@app.post("/api/chat", response_model=ChatResponse)
def chat_ai(query_data: ChatQuery):
    """
    Intelligent endpoint processing recruiter and visitor questions.
    """
    q = query_data.query.lower().strip()
    
    if any(k in q for k in ["who", "about", "rakesh", "bio"]):
        reply = (
            f"{PROFILE_DATA['name']} is a passionate {PROFILE_DATA['title']} studying "
            f"{PROFILE_DATA['education']['degree']} ({PROFILE_DATA['education']['stream']}) "
            f"at {PROFILE_DATA['education']['institution']} with an impressive CGPA of "
            f"{PROFILE_DATA['education']['cgpa']}."
        )
    elif any(k in q for k in ["skill", "tech", "python", "fastapi", "stack", "machine learning"]):
        all_skills = ", ".join(
            PROFILE_DATA['skills']['programming'] + 
            PROFILE_DATA['skills']['ai_ml'] + 
            PROFILE_DATA['skills']['backend']
        )
        reply = f"Rakesh specializes in: {all_skills}. He builds production-ready FastAPI backends and applied AI systems."
    elif any(k in q for k in ["project", "chatbot", "face", "game", "tic tac"]):
        project_titles = [f"{p['name']} ({p['tech']})" for p in PROFILE_DATA['projects']]
        reply = f"Rakesh has engineered standout AI projects including: {'; '.join(project_titles)}."
    elif any(k in q for k in ["cgpa", "college", "university", "education", "score", "grade"]):
        reply = (
            f"Rakesh attends {PROFILE_DATA['education']['institution']} for {PROFILE_DATA['education']['degree']}. "
            f"His current academic score is {PROFILE_DATA['education']['cgpa']}."
        )
    elif any(k in q for k in ["contact", "email", "phone", "reach", "hire", "number"]):
        reply = (
            f"You can reach Rakesh via Email: {PROFILE_DATA['contact']['email']} or "
            f"Phone: {PROFILE_DATA['contact']['phone']}. He is actively interviewing for AI/ML Engineer positions!"
        )
    elif any(k in q for k in ["cert", "drone", "fly smart", "achievement"]):
        cert = PROFILE_DATA['certifications'][0]
        reply = f"Rakesh participated in {cert['title']} organized by {cert['organization']} ({cert['year']})."
    else:
        reply = (
            f"Rakesh Pal is an AI/ML Engineer skilled in Python, Machine Learning, Computer Vision, and FastAPI. "
            f"You can check out his projects on the portfolio or email him at {PROFILE_DATA['contact']['email']}."
        )

    return ChatResponse(
        query=query_data.query,
        response=reply,
        timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
    )

@app.post("/api/contact")
def submit_contact(msg: ContactMessage):
    """Receives contact messages from the portfolio website."""
    return {
        "status": "received",
        "message": f"Thank you, {msg.name}! Your message has been noted.",
        "details": msg.model_dump()
    }
