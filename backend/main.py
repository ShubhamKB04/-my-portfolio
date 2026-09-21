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
    title="Rakesh Pal Portfolio AI API",
    description="Backend API powering Rakesh Pal's AI Portfolio and Recruiter Assistant",
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
    "name": "Rakesh Pal",
    "title": "AI/ML Engineer",
    "specialization": "Artificial Intelligence & Machine Learning",
    "location": "Kolkata, West Bengal, India",
    "contact": {
        "email": "rakeshpal932004@gmail.com",
        "phone": "+91-7501678411",
        "github": "https://github.com",
        "linkedin": "https://linkedin.com"
    },
    "education": {
        "degree": "B.Tech in Computer Science & Engineering",
        "stream": "Artificial Intelligence & Machine Learning",
        "institution": "Brainware University, Kolkata",
        "duration": "2023 – 2027",
        "cgpa": "8.07 / 10 (through 6th Semester)"
    },
    "skills": {
        "programming": ["Python", "JavaScript"],
        "ai_ml": ["Machine Learning", "NLP", "Generative AI", "Computer Vision"],
        "data_science": ["Pandas", "NumPy", "Scikit-learn"],
        "backend": ["FastAPI", "REST APIs", "Streamlit"],
        "tools": ["Git", "GitHub", "Docker", "VS Code"]
    },
    "projects": [
        {
            "id": "chatbot",
            "name": "Rule-Based Chatbot",
            "tech": "Python, Streamlit, NLP",
            "summary": "Interactive rule-based conversational logic with session-based memory.",
            "file": "rule_based_chatbot.py"
        },
        {
            "id": "facedetection",
            "name": "Face Detection AI",
            "tech": "Python, OpenCV, Computer Vision",
            "summary": "Real-time face detection across images and video feeds with coordinate tracking."
        },
        {
            "id": "tictactoe",
            "name": "Tic-Tac-Toe AI",
            "tech": "Python, Minimax Algorithm, Game Logic",
            "summary": "Unbeatable AI opponent powered by recursive game state search."
        }
    ],
    "certifications": [
        {
            "title": "FLY SMART — AI Drone Innovation Camp 2026",
            "organization": "Brainware University",
            "year": 2026
        }
    ],
    "career_target": {
        "role": "AI/ML Engineer — Fresher / Junior",
        "focus": ["Machine Learning", "Generative AI", "NLP", "Computer Vision", "Python", "FastAPI"]
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
