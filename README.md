 # 🧠 EmoCare: AI Wellness Companion 🧘🏻‍♀️

> *An AI-powered, empathetic conversational agent built to provide gentle support and a safe space for self-reflection.*

---

## 📌 Project Status
**Framework:** Complete ✅  
**Course:** Data 690 – Special Topics in AI  
**Tech Stack:** Streamlit · Groq · ElevenLabs  

---

## ✨ Overview

**EmoCare** is more than a chatbot — it’s a personalized wellness companion designed to help users process emotions, discover healthy coping strategies, and reflect mindfully in a **non-judgmental, supportive environment**.

This project was developed as part of **Data 690: Special Topics in AI**, under the guidance of **Prof. Levan Sulimanov**, with a focus on applying modern AI responsibly in the mental wellness domain.

---

## 🚀 Key Features

### 🎨 Custom Theming
- Warm, minimal, and calming UI  
- Built using **Streamlit custom CSS (`wellness.css`)** for a cozy wellness-focused experience

### 💬 Conversational AI
- Powered by **Groq’s high-speed LLM API (Llama 3.1)**  
- Delivers fast, empathetic, and context-aware responses  
- Adapts replies based on user-selected **mood** and **focus area**

### 🎙️ Voice Mode (STT & 🔊 TTS)
- Hands-free interaction via **ElevenLabs**
- **Speech-to-Text (STT)** for voice input  
- **Text-to-Speech (TTS)** for natural, calming voice responses

### 📖 Personalized Context
- Upload personal **journal / notes PDFs**
- EmoCare uses them as contextual grounding  
- Auto-generated **Word Cloud** for visual emotional insights

### 🧭 Action Compass
- Dynamic sidebar offering **gentle, mood-based nudges**
- Example:  
  > *Angry → 🎵 Sing it out*

### 🌿 Calm Quest Mini‑Game
A 60‑second guided reset consisting of:
1. 🫁 Breathing timer  
2. 🎯 Focus exercise  
3. ✍️ One-line journaling prompt  

### 🎧 Mood‑Based Music
- Curated **YouTube playlist recommendations**
- Automatically matched to the user’s selected mood

---

## 🆕 Updates: Facial Emotion Detection (Jetson Nano)

EmoCare has been extended with **real-time facial emotion detection** using a webcam, designed to run efficiently on **edge devices such as NVIDIA Jetson Nano**.

### 🔍 What’s Added
EmoCare uses lightweight, ONNX-based computer vision models for real-time facial emotion detection, optimized for edge devices:
- Live **face detection** using **OpenCV YuNet (ONNX)**
- **Facial emotion classification** using the **FER+ ONNX model**
- Emotion label + confidence score displayed on the camera feed
- Largest detected face is selected for emotion inference (more stable results)
Both models run locally on-device using OpenCV’s DNN module, ensuring low latency, privacy preservation, and compatibility with NVIDIA Jetson Nano.

### 😊 Detected Emotions (FER+)
- neutral
- happiness
- surprise
- sadness
- anger
- disgust
- fear
- contempt

### ⚙️ Jetson-Friendly Optimizations
- Emotion inference runs **every 5 frames** (reduces compute load)
- Camera resolution capped at **640×480**
- Uses **V4L2 backend** for better USB webcam compatibility
- Requests **MJPEG** stream when supported
- Stores last emotion to avoid flicker between inference frames
- Camera runs in **time-limited sessions** and releases resources automatically

### 📁 Required Models
Place the following files inside a `models/` folder:

```text
models/
├── face_detection_yunet_2023mar.onnx
└── emotion-ferplus-8.onnx
```

🔒 Privacy Note

All emotion inference happens locally on-device. No camera frames are uploaded or stored by EmoCare.

---

### 🖼️ App Interface Preview

A glimpse into EmoCare’s calming, voice-enabled, and user-centric wellness experience.

<table>
  <tr>
    <!-- LEFT COLUMN: MAIN UI + CHAT (LARGER) -->
    <td width="60%" align="center" valign="top">
      <img src="app-look/EmoCareUI.png"
           width="92%"
           alt="EmoCare main wellness interface" />
      <br/><br/>
      <img src="app-look/EmoCareChatbot.png"
           width="92%"
           alt="EmoCare chat and conversation interface" />
    </td>
    <!-- RIGHT COLUMN: SIDEBAR + CAMERA (COMPACT & BALANCED) -->
    <td width="30%" align="center" valign="top">
      <img src="app-look/EmoCareSidebar.png"
           width="85%"
           alt="EmoCare sidebar with music, journal upload, and tools" />
      <br/><br/>
      <img src="app-look/EmoCareCam.png"
           width="85%"
           style="max-height: 320px; object-fit: contain;"
           alt="EmoCare facial emotion detection camera view" />
    </td>
  </tr>
</table>


---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd emacare
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
> ⚠️ Requires **ffmpeg** to be installed for `ffmpeg-python`

### 3️⃣ Configure Environment Variables
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=gsk_...
ELEVENLABS_API_KEY=sk_...
```

**API Usage**
- `GROQ_API_KEY` → Core conversational LLM logic  
- `ELEVENLABS_API_KEY` → Voice Mode (STT & TTS)

### 4️⃣ Run the Application
```bash
streamlit run wellness.py
```

---

## 🐛 Troubleshooting & Solutions

| Problem Encountered | Solution |
|-------------------|----------|
| **ElevenLabs TTS Output Stream** | SDK sometimes returns a generator instead of bytes. Fixed using:<br>`b"".join(chunk for chunk in audio_result)` |
| **ElevenLabs STT Model ID** | Transcription failed with generic IDs. Explicitly used **`scribe_v1`**, optimized for STT |
| **sounddevice Device Selection** | Stored device IDs in `st.session_state` and set:<br>`sd.default.device = (input_id, output_id)` |
| **Streamlit Button Reruns** | Required immediate state updates and `st.rerun()` for UI step transitions |

---

## 🖼️ UI & Response Examples

### 💬 EmoCare Response Example

**User (Voice):**  
> *"I feel like I have too much on my plate this week. My boss gave me two huge deadlines and I haven't slept well."*

**EmoCare:**  
> *"That sounds like a heavy load to carry right now. It’s completely understandable that you’re feeling overwhelmed and losing sleep. Your worth isn’t tied to productivity. Could you try one small act of self‑care — maybe stepping away for 90 seconds and stretching? Is there one meeting you could postpone or one small task you could delegate to give yourself a little more room to breathe?"*

---

### 🧭 Action Compass Example

When the user selects **Stressed / Overwhelmed**, EmoCare highlights:

```html
<div class="compass-swatch active">
  <b>Stressed</b> → 🏃 Move your body – even 60 seconds counts
</div>
```

---

## 🙏 Acknowledgements

- **Prof. Levan Sulimanov**  
  For the academic framework and inspiration to explore ethical AI in mental wellness  

- **Groq**  
  For blazing-fast LLM inference enabling real-time, supportive conversations  

- **ElevenLabs**  
  For high-quality Speech-to-Text and Text-to-Speech APIs  

- **Streamlit**  
  For making it possible to build a professional-grade AI web app entirely in Python  

---

🌱 *Built with empathy, responsibility, and human-centered AI in mind.*
