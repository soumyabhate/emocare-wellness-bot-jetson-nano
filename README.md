
# 🧠 EmoCare: AI Wellness Companion 🧘🏻‍♀️

> *An AI-powered, empathetic wellness companion designed to provide gentle emotional support, self-reflection tools, and real-time emotion awareness.*

---

## 📌 Project Status
**Framework:** Complete ✅  
**Course:** Data 690 – Special Topics in AI  
**Focus Areas:** Conversational AI · Mental Wellness · Edge AI  
**Deployment:** Streamlit (Web) + Jetson Nano (Edge-ready)
**Instructor:** Prof. Levan Sulimanov

---

## ✨ Overview

**EmoCare** is more than a chatbot — it is a **human-centered AI wellness companion** that helps users reflect on emotions, manage stress, and engage in mindful self-check-ins in a **non-judgmental and supportive environment**.

The system combines:
- Conversational AI
- Voice interaction
- Visual emotion sensing
- Gentle behavioral nudges

This project was developed as part of **Data 690: Special Topics in AI**, under the guidance of **Prof. Levan Sulimanov**, with a strong emphasis on **ethical, responsible AI** for mental wellness.

---

## 🚀 Core Features

### 💬 Conversational Wellness AI
- Powered by **Groq LLM (Llama 3.x)**
- Emotion-aware, empathetic responses
- Contextual grounding using mood, focus area, and optional journal input

### 🎙️ Voice Mode (STT & 🔊 TTS)
- Speech-to-Text and Text-to-Speech using **ElevenLabs**
- Optional, user-controlled voice interaction

### 📖 Journal-Aware Reflection
- Upload personal PDFs (journals/notes)
- Automatic anonymization
- Optional word cloud visualization

### 🎮 Calm Quest Mini-Game
- 60-second guided grounding experience
- Breathing, grounding, and journaling

### 🎧 Mood-Based Music Recommendations
- YouTube playlist suggestions based on mood

### 🧭 Action Compass
- Gentle, emotion-based nudges (not prescriptive)

---

## 🔍 Update: Real-Time Facial Emotion Detection (NEW)

### 📷 What Was Added
- Live facial emotion detection using webcam
- Optimized for **NVIDIA Jetson Nano**
- Fully local, privacy-preserving inference

### 🧠 Technical Pipeline
**Face Detection:** OpenCV YuNet (ONNX)  
**Emotion Model:** FER+ (ONNX)

Recognized emotions:
`neutral, happiness, surprise, sadness, anger, disgust, fear, contempt`

### ⚡ Performance Optimizations
- Emotion inference every 5 frames
- Resolution capped at 640×480
- MJPEG + V4L2 backend
- 10-second controlled camera sessions

### 🔒 Privacy
- No video storage
- No external transmission
- Explicit user control

### 📦 Required Models
```
models/
├── face_detection_yunet_2023mar.onnx
└── emotion-ferplus-8.onnx
```

---

## 🛠️ Installation & Setup

```bash
git clone <your-repo-link>
cd emocare
pip install -r requirements.txt
streamlit run wellness.py
```

Create a `.env` file:
```env
GROQ_API_KEY=...
ELEVENLABS_API_KEY=...
```

---

## 🔮 Future Work
- Multi-face tracking
- Emotion smoothing
- Text + Voice + Face fusion
- Offline Jetson-only mode

---

## 🙏 Acknowledgements
- Prof. Levan Sulimanov
- Groq
- ElevenLabs
- Streamlit

---

🌱 *Built with empathy, responsibility, and human-centered AI in mind.*
