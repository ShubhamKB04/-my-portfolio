/**
 * Rakesh Pal - AI/ML Engineer Portfolio Script
 * Interactive UI, Typing Animation, Project Modals & AI Chat Assistant
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Dynamic Typing Effect
  const phrases = [
    'AI & Machine Learning Systems.',
    'High-Performance FastAPI Backends.',
    'Computer Vision Applications.',
    'Generative AI & Conversational Bots.',
    'Decision-Making Game AI.'
  ];
  let phraseIndex = 0;
  let letterIndex = 0;
  let isDeleting = false;
  const typedTextEl = document.getElementById('typedText');

  function typeEffect() {
    if (!typedTextEl) return;
    const currentPhrase = phrases[phraseIndex];
    
    if (isDeleting) {
      typedTextEl.textContent = currentPhrase.substring(0, letterIndex - 1);
      letterIndex--;
    } else {
      typedTextEl.textContent = currentPhrase.substring(0, letterIndex + 1);
      letterIndex++;
    }

    let typeSpeed = isDeleting ? 40 : 80;

    if (!isDeleting && letterIndex === currentPhrase.length) {
      typeSpeed = 1800; // Pause at end of sentence
      isDeleting = true;
    } else if (isDeleting && letterIndex === 0) {
      isDeleting = false;
      phraseIndex = (phraseIndex + 1) % phrases.length;
      typeSpeed = 400;
    }

    setTimeout(typeEffect, typeSpeed);
  }
  typeEffect();

  // 2. Mobile Menu Toggle
  const menuToggle = document.getElementById('menuToggle');
  const navLinks = document.getElementById('navLinks');
  if (menuToggle && navLinks) {
    menuToggle.addEventListener('click', () => {
      const isVisible = navLinks.style.display === 'flex';
      navLinks.style.display = isVisible ? 'none' : 'flex';
      if (!isVisible) {
        navLinks.style.flexDirection = 'column';
        navLinks.style.position = 'absolute';
        navLinks.style.top = '76px';
        navLinks.style.left = '0';
        navLinks.style.right = '0';
        navLinks.style.background = 'rgba(7, 9, 14, 0.95)';
        navLinks.style.padding = '24px';
        navLinks.style.borderBottom = '1px solid rgba(255,255,255,0.1)';
      }
    });
  }

  // 3. Project Deep-Dive Modal Data
  const projectDetails = {
    chatbot: {
      title: 'Rule-Based Conversational Chatbot',
      tag: 'Python • Streamlit • NLP Rule Logic',
      description: 'An interactive conversational chatbot built from the ground up using Python and Streamlit. Designed with clear decision trees, regex pattern matching, and intent classification to handle complex user queries seamlessly.',
      highlights: [
        'Modular rule engine that categorizes intents into greetings, project queries, technical FAQs, and fallbacks.',
        'Interactive Streamlit UI with conversation memory, avatar icons, and session history.',
        'Engineered for low latency and zero external API dependencies for guaranteed local privacy.',
        'File structure: rule_based_chatbot.py with clean function separation.'
      ],
      stack: ['Python 3', 'Streamlit', 'Regex', 'Session State Management']
    },
    facedetection: {
      title: 'Real-Time Face Detection AI',
      tag: 'Python • OpenCV • Computer Vision',
      description: 'An applied computer vision system that detects faces from static images or live camera video streams in real-time using pre-trained feature cascades and image processing pipelines.',
      highlights: [
        'Image preprocessing: greyscale conversion, histogram equalization, and multi-scale detection parameters.',
        'Real-time bounding box projection with confidence thresholds and coordinates extraction.',
        'Optimized frame-rate throughput suitable for edge devices or embedded camera hardware.',
        'Demonstrates mastery of core computer vision principles and OpenCV algorithms.'
      ],
      stack: ['Python', 'OpenCV', 'NumPy', 'Computer Vision']
    },
    tictactoe: {
      title: 'Tic-Tac-Toe AI with Minimax Algorithm',
      tag: 'Python • Game AI • Minimax Tree Search',
      description: 'An intelligent AI opponent for Tic-Tac-Toe that calculates optimal moves using game theory and recursive Minimax tree evaluation, making the AI mathematically unbeatable.',
      highlights: [
        'Recursive state-space tree traversal evaluating all potential future game outcomes.',
        'Terminal state evaluation (+10 win, -10 loss, 0 draw) with depth-based penalization for rapid wins.',
        'Clean terminal and interactive CLI interface with move validation and board rendering.',
        'Foundation for deeper exploration into reinforcement learning and search algorithms.'
      ],
      stack: ['Python', 'Minimax Algorithm', 'Game Theory', 'State Space Search']
    }
  };

  const projectModal = document.getElementById('projectModal');
  const modalBody = document.getElementById('modalBody');
  const modalCloseBtn = document.getElementById('modalCloseBtn');

  document.querySelectorAll('.modal-trigger').forEach(btn => {
    btn.addEventListener('click', () => {
      const key = btn.getAttribute('data-project');
      const data = projectDetails[key];
      if (data && modalBody && projectModal) {
        modalBody.innerHTML = `
          <div style="margin-bottom: 12px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--primary);">${data.tag}</div>
          <h2 style="color: #fff; font-size: 1.8rem; margin-bottom: 16px;">${data.title}</h2>
          <p style="color: var(--text-muted); font-size: 1rem; line-height: 1.7; margin-bottom: 20px;">${data.description}</p>
          <h4 style="color: #fff; font-size: 1rem; margin-bottom: 12px;">Key Engineering Highlights:</h4>
          <ul style="list-style: none; margin-bottom: 24px;">
            ${data.highlights.map(h => `<li style="display: flex; gap: 8px; color: var(--text-muted); margin-bottom: 10px; font-size: 0.9rem;"><span style="color: var(--accent-emerald)">✓</span> ${h}</li>`).join('')}
          </ul>
          <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 24px;">
            ${data.stack.map(s => `<span class="stack-tag">${s}</span>`).join('')}
          </div>
          <div style="display: flex; gap: 12px;">
            <a href="https://github.com" target="_blank" class="btn-primary" style="font-size: 0.9rem; padding: 10px 20px;">View on GitHub</a>
            <button class="btn-secondary" onclick="document.getElementById('projectModal').classList.remove('active')" style="font-size: 0.9rem; padding: 10px 20px;">Close Window</button>
          </div>
        `;
        projectModal.classList.add('active');
      }
    });
  });

  if (modalCloseBtn && projectModal) {
    modalCloseBtn.addEventListener('click', () => projectModal.classList.remove('active'));
    projectModal.addEventListener('click', (e) => {
      if (e.target === projectModal) projectModal.classList.remove('active');
    });
  }

  // 4. Contact Form Submission
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const message = document.getElementById('message').value;

      const submitBtn = document.getElementById('submitContactBtn');
      submitBtn.innerHTML = '<span>Message Sent! ✓</span>';
      submitBtn.style.background = '#10b981';
      submitBtn.style.color = '#fff';

      setTimeout(() => {
        // Open prefilled mail client
        const mailtoUri = `mailto:rakeshpal932004@gmail.com?subject=Contact from Portfolio: ${encodeURIComponent(name)}&body=${encodeURIComponent(`Name: ${name}\nEmail: ${email}\n\n${message}`)}`;
        window.location.href = mailtoUri;

        contactForm.reset();
        submitBtn.innerHTML = `<span>Send Message</span><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>`;
        submitBtn.style.background = '';
        submitBtn.style.color = '';
      }, 1200);
    });
  }

  // 5. Intelligent AI Recruiter Chatbot
  const chatToggle = document.getElementById('chatToggle');
  const chatWindow = document.getElementById('chatWindow');
  const chatCloseBtn = document.getElementById('chatCloseBtn');
  const chatInput = document.getElementById('chatInput');
  const chatSendBtn = document.getElementById('chatSendBtn');
  const chatMessages = document.getElementById('chatMessages');
  const triggerAiChatBtn = document.getElementById('triggerAiChatBtn');

  function toggleChat() {
    if (chatWindow) {
      chatWindow.classList.toggle('active');
      if (chatWindow.classList.contains('active')) {
        chatInput?.focus();
      }
    }
  }

  chatToggle?.addEventListener('click', toggleChat);
  triggerAiChatBtn?.addEventListener('click', toggleChat);
  chatCloseBtn?.addEventListener('click', () => chatWindow?.classList.remove('active'));

  // Knowledge base for instant client-side answers
  const portfolioKnowledge = {
    who: "Rakesh Pal is an aspiring AI/ML Engineer and B.Tech CSE (AI & ML) student at Brainware University, Kolkata (Graduation 2027). He holds an 8.07/10 CGPA through 6th semester.",
    skills: "Rakesh's technical skills include:\n• Programming: Python, JavaScript\n• AI & ML: Machine Learning, NLP, Generative AI, Computer Vision\n• Data Science: Pandas, NumPy, Scikit-learn\n• Backend & APIs: FastAPI, REST APIs\n• DevOps & Tools: Git, GitHub, Docker, VS Code.",
    projects: "Rakesh has developed three standout projects:\n1. Rule-Based Chatbot (Python & Streamlit conversational system)\n2. Face Detection AI (Real-time computer vision with OpenCV)\n3. Tic-Tac-Toe AI (Decision-tree Minimax game algorithm).",
    education: "Rakesh is pursuing a B.Tech in Computer Science & Engineering (Artificial Intelligence & Machine Learning) at Brainware University, Kolkata (2023–2027) with an 8.07/10 CGPA.",
    contact: "You can reach Rakesh directly at:\n• Email: rakeshpal932004@gmail.com\n• Phone: +91-7501678411\n• Location: Kolkata, West Bengal, India.",
    certification: "Rakesh successfully participated in the FLY SMART — AI Drone Innovation Camp 2026 at Brainware University, focusing on AI navigation and drone technologies.",
    hire: "Rakesh is targeting Fresher / Junior AI/ML Engineer and Backend API roles. He is passionate, industry-ready, and available for full-time opportunities or internships!"
  };

  function getLocalResponse(query) {
    const q = query.toLowerCase();
    if (q.includes('who') || q.includes('about') || q.includes('rakesh') || q.includes('bio')) {
      return portfolioKnowledge.who;
    } else if (q.includes('skill') || q.includes('tech') || q.includes('python') || q.includes('stack') || q.includes('fastapi')) {
      return portfolioKnowledge.skills;
    } else if (q.includes('project') || q.includes('chatbot') || q.includes('face') || q.includes('game') || q.includes('tic tac')) {
      return portfolioKnowledge.projects;
    } else if (q.includes('cgpa') || q.includes('college') || q.includes('university') || q.includes('education') || q.includes('brainware') || q.includes('score')) {
      return portfolioKnowledge.education;
    } else if (q.includes('contact') || q.includes('email') || q.includes('phone') || q.includes('reach') || q.includes('call') || q.includes('number')) {
      return portfolioKnowledge.contact;
    } else if (q.includes('cert') || q.includes('drone') || q.includes('achievement') || q.includes('fly smart')) {
      return portfolioKnowledge.certification;
    } else if (q.includes('hire') || q.includes('job') || q.includes('role') || q.includes('fresher') || q.includes('work')) {
      return portfolioKnowledge.hire;
    } else {
      return `Thanks for asking! Rakesh specializes in Python, Machine Learning, Computer Vision, and FastAPI. Feel free to download his resume or email him directly at rakeshpal932004@gmail.com!`;
    }
  }

  async function handleSendMessage(text) {
    const query = text || chatInput?.value?.trim();
    if (!query || !chatMessages) return;

    // Append User Message
    const userMsgDiv = document.createElement('div');
    userMsgDiv.className = 'chat-msg msg-user';
    userMsgDiv.textContent = query;
    chatMessages.appendChild(userMsgDiv);

    if (chatInput) chatInput.value = '';
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // Loading indicator
    const botLoadingDiv = document.createElement('div');
    botLoadingDiv.className = 'chat-msg msg-bot';
    botLoadingDiv.textContent = 'Thinking...';
    chatMessages.appendChild(botLoadingDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // Check if FastAPI backend is available
    let botReply = '';
    try {
      const response = await fetch('http://127.0.0.1:8000/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: query }),
        signal: AbortSignal.timeout(1200) // quick timeout to failover gracefully
      });
      if (response.ok) {
        const data = await response.json();
        botReply = data.response;
      } else {
        botReply = getLocalResponse(query);
      }
    } catch {
      // Backend not running, fall back gracefully to local engine
      botReply = getLocalResponse(query);
    }

    botLoadingDiv.innerText = botReply;
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  chatSendBtn?.addEventListener('click', () => handleSendMessage());
  chatInput?.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') handleSendMessage();
  });

  document.querySelectorAll('.chip').forEach(chip => {
    chip.addEventListener('click', () => {
      const query = chip.getAttribute('data-query');
      if (query) handleSendMessage(query);
    });
  });
});
