# 🚀 Rakesh Pal — AI/ML Engineer Portfolio Website

A futuristic, high-performance personal portfolio website engineered for **Rakesh Pal** (AI/ML Engineer, B.Tech CSE AI & ML at Brainware University).

Featuring modern glassmorphism design, cyber glowing accents, interactive AI project showcases, real-time recruiter assistant chatbot, and a Python **FastAPI** backend API.

---

## 📁 Project Directory Structure

```text
d:\Deployment\Rakesh-Portfolio\
├── index.html              # Main HTML5 webpage (Hero, About, Skills, Projects, Contact, Chatbot)
├── style.css               # Futuristic Dark Cyber CSS stylesheet (Glassmorphism & Responsive)
├── app.js                  # Interactive logic: Dynamic typing, project modals & AI Chatbot
├── .gitignore              # Files to ignore in Git
├── README.md               # This complete step-by-step guide
├── assets/
│   ├── profile.jpg         # Your professional portrait photograph
│   └── Rakesh_Pal_Resume.pdf # Your downloadable resume PDF
└── backend/
    ├── main.py             # Python FastAPI REST API with AI endpoints
    ├── requirements.txt    # Python dependencies (fastapi, uvicorn, pydantic)
    └── run.bat             # 1-Click Windows script to start the AI Backend
```

---

## 💻 STEP 1: How to Open & Edit in VS Code

### 1. Open the Project Folder
1. Open **Visual Studio Code (VS Code)**.
2. Click **File** > **Open Folder...** (or press `Ctrl + K`, then `Ctrl + O`).
3. Select `D:\Deployment\Rakesh-Portfolio` and click **Select Folder**.
4. You will see all your files on the left sidebar (**Explorer**).

### 2. How to Create New Files in VS Code
- In the left sidebar next to the word **RAKESH-PORTFOLIO**, click the **New File** icon (📄 with a `+`).
- Type the file name (e.g., `test.py` or `notes.txt`) and press **Enter**.

### 3. How to Edit Your Information
- To change your bio, university, or links: open [`index.html`](file:///d:/Deployment/Rakesh-Portfolio/index.html).
- To customize colors or font sizes: open [`style.css`](file:///d:/Deployment/Rakesh-Portfolio/style.css).
- To add more chatbot answers: open [`app.js`](file:///d:/Deployment/Rakesh-Portfolio/app.js) or [`backend/main.py`](file:///d:/Deployment/Rakesh-Portfolio/backend/main.py).

---

## ⚡ STEP 2: How to Run This Project Locally

### Option A: Direct Double Click (Zero Install Needed!)
1. Open Windows File Explorer and navigate to `D:\Deployment\Rakesh-Portfolio`.
2. Double click **`index.html`**.
3. It will open instantly in your default web browser (Chrome, Edge, etc.)!

### Option B: Using VS Code "Live Server" (Recommended for Development)
1. Inside VS Code, click the **Extensions** icon on the far left bar (or press `Ctrl + Shift + X`).
2. Search for **Live Server** (by Ritwick Dey) and click **Install**.
3. Right-click on [`index.html`](file:///d:/Deployment/Rakesh-Portfolio/index.html) in the file list and choose **"Open with Live Server"**.
4. Your website will open at `http://127.0.0.1:5500/index.html`. Any edits you make and save in VS Code will update live in your browser!

---

## 🤖 STEP 3: How to Run the Python FastAPI AI Backend (Optional)

Your portfolio has a built-in AI chatbot that works offline right out of the box. You can also run the Python FastAPI backend to test real REST API interactions:

1. Make sure Python is installed on your computer from [python.org](https://www.python.org/downloads/) (Make sure to check *"Add python.exe to PATH"* during install).
2. Open the `backend/` folder.
3. Double click **`run.bat`** (or open terminal in VS Code and run `python -m pip install -r backend/requirements.txt`, then `uvicorn backend.main:app --reload`).
4. Visit `http://127.0.0.1:8000/docs` in your browser to test the interactive Swagger API documentation!

---

## 🐙 STEP 4: How to Upload to Git & GitHub

### 1. Download & Install Git
If you don't have Git installed yet:
1. Go to [https://git-scm.com/download/win](https://git-scm.com/download/win) and download the 64-bit Windows installer.
2. Run the installer (keep default options) and finish installation.
3. Restart VS Code so it recognizes Git.

### 2. Create a GitHub Account & Repository
1. Log in to [GitHub.com](https://github.com).
2. In the top right corner, click the **`+`** icon > **New repository**.
3. Repository name: `rakesh-portfolio` (or `portfolio`).
4. Set visibility to **Public**.
5. Do **NOT** check "Add a README file" (we already have one).
6. Click **Create repository**.
7. Copy the repository URL (e.g. `https://github.com/your-username/rakesh-portfolio.git`).

### 3. Initialize & Push from VS Code Terminal
1. Inside VS Code, open the built-in terminal by pressing **`Ctrl + \``** (or click **Terminal** > **New Terminal**).
2. Run these commands one by one:

```bash
# 1. Set your Git username and email
git config --global user.name "Rakesh Pal"
git config --global user.email "rakeshpal932004@gmail.com"

# 2. Initialize git repository
git init

# 3. Add all files
git add .

# 4. Commit files
git commit -m "Initial commit: Rakesh Pal AI Portfolio with photo, resume, and FastAPI backend"

# 5. Rename branch to main
git branch -M main

# 6. Link to your GitHub repository (replace URL with your own repo URL!)
git remote add origin https://github.com/your-username/rakesh-portfolio.git

# 7. Push your code to GitHub
git push -u origin main
```

---

## 🌐 STEP 5: How to Host It Online for FREE with GitHub Pages

Once your code is pushed to GitHub, you can publish it live on the internet in 3 clicks:

1. On your GitHub repository page, click on **Settings** (tab at the top).
2. In the left menu under "Code and automation", click **Pages**.
3. Under **Build and deployment** > **Branch**:
   - Change `None` to **`main`**.
   - Folder: leave as **`/(root)`**.
   - Click **Save**.
4. Wait 1–2 minutes, then refresh the page.
5. GitHub will provide your live URL:
   **`https://your-username.github.io/rakesh-portfolio/`**
6. Anyone in the world (recruiters, professors, friends) can now visit your live portfolio!

---

## 💼 STEP 6: How to Add to LinkedIn to Attract AI/ML Recruiters

### 1. Update Your LinkedIn Headline
Change your headline to:
> **B.Tech CSE (AI & ML) @ Brainware University | AI/ML Engineer Fresher | Python • FastAPI • Computer Vision • NLP**

### 2. Add to Your LinkedIn "Featured" Section
1. Go to your LinkedIn profile.
2. Click **Add profile section** > **Recommended** > **Add featured**.
3. Click the **`+`** icon > **Add a link**.
4. Paste your live GitHub Pages link: `https://your-username.github.io/rakesh-portfolio/`.
5. Title: **Rakesh Pal — AI/ML Engineer Portfolio Website**.
6. Description: *Interactive personal portfolio showcasing my AI projects (Rule-Based Chatbot, Real-time Face Detection AI, Tic-Tac-Toe Minimax AI), technical skills, and resume.*

### 3. Share a Professional LinkedIn Post
Create a new post with your screenshot or photo and this template:

```text
🚀 Excited to unveil my new AI & Machine Learning Portfolio! 🤖

As a B.Tech CSE student specializing in Artificial Intelligence & Machine Learning at Brainware University (8.07 CGPA), I am passionate about engineering intelligent systems that bridge theoretical AI with practical, high-performance applications.

✨ What's inside my portfolio:
💬 Conversational Rule-Based Chatbot (Python & Streamlit)
👁️ Real-Time Face Detection AI (Computer Vision & OpenCV)
🎮 Minimax Game AI (Decision Tree & State Search)
⚡ Python FastAPI Backend REST API with an embedded AI Assistant
📄 Direct Resume download & interactive project deep-dives

🔗 Live Portfolio: [Insert Your GitHub Pages Link]
💻 GitHub Repository: [Insert Your GitHub Repo Link]

I am actively seeking AI/ML Engineer (Fresher / Junior) opportunities and internships. Let's connect!

#ArtificialIntelligence #MachineLearning #Python #FastAPI #ComputerVision #DeepLearning #WebDevelopment #Portfolio #JobSearch #BrainwareUniversity #FresherHiring
```

---

## ✉️ Contact Information
- **Full Name:** Rakesh Pal
- **Email:** [rakeshpal932004@gmail.com](mailto:rakeshpal932004@gmail.com)
- **Phone:** +91-7501678411
- **Location:** Kolkata, West Bengal, India
- **University:** Brainware University (2023 – 2027)
