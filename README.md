# EmoCare Therapy Bot 🧠💬🎧

> **Status:** Components are currently **not connected** end‑to‑end. Each file works **separately**.  
> **Next step:** **Integrate** voice recording → STT → LLM → TTS → Streamlit UI into one flow. 🚀

---

## 📌 What is this?

A starter kit for an emotion-aware therapy bot. The repo includes:
- A **Streamlit UI** prototype
- **Voice recording** utility
- **Speech-to-text** (SR) scaffolding
- **Text-to-speech** (TTS) hooks
- Sample audio files

Right now, these pieces run **individually**. The plan is to **wire them together** next.

---

## 🗂️ Repository Structure

```
EmoCare Therapy Bot/
├─ .venv/                      # Local virtual environment (optional)
├─ .env                        # Your secrets (not committed) – optional
├─ README.md                   # This file
├─ requirements.txt            # Python dependencies
├─ bot.py                      # Main LLM workflow (renamed from Yipeeeee.py); may include Streamlit UI sections
├─ bot_ui.py                   # Alternate/minimal Streamlit UI shell
├─ streamlit.ipynb             # Notebook used to design UI
├─ record_test.py              # Mic → WAV recorder & playback test
├─ avatar_output.mp3           # Sample output audio
├─ soumya_input.mp3            # Sample input audio
└─ (others)                    # e.g., __pycache__, assets, etc.
```
> ⚠️ **Important:** Don’t keep a file named `streamlit.py` in this folder—  
> it shadows the real `streamlit` library and causes import errors.

---

## 🧰 Tech Stack

- **Frontend:** Streamlit 🖥️  
- **Audio I/O:** `sounddevice`, `PyAudio` 🎙️  
- **STT (Speech-to-Text):** `SpeechRecognition` (file/mic) 🗣️→📝  
- **LLM (reasoning):** Groq API (planned) 🤖  
- **TTS (Text-to-Speech):** ElevenLabs API (planned) 📝→🔊  
- **Utils:** `ffmpeg-python`, `python-dotenv`, `numpy`, `scipy`

---

## ✅ Prerequisites

- **Python 3.10/3.11**
- **FFmpeg** installed & on PATH  
  - Windows: install via `choco install ffmpeg` *or* download from ffmpeg.org  
  - macOS: `brew install ffmpeg`  
  - Ubuntu: `sudo apt-get install -y ffmpeg`
- **(Windows mic)** `PyAudio` (we’ll install below).  
  macOS/Linux often use PortAudio system libs.

---

## ⚙️ Setup

### Windows (PowerShell)
```powershell
# 1) Open folder in VS Code and create a venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2) Install Python packages
python -m pip install --upgrade pip
pip install -r requirements.txt

# If you see SR/PyAudio errors:
pip install SpeechRecognition
pip install pyaudio==0.2.13 --only-binary=:all:
# (If that fails, try without --only-binary)
```

### macOS/Linux (bash/zsh)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🔐 Environment Variables (Optional but Recommended)

Create a file named `.env` in the project root:
```
GROQ_API_KEY=sk_groq_...
ELEVEN_API_KEY=your_eleven_key
ELEVEN_VOICE_ID=21m00Tcm4TlvDq8ikWAM
DEBUG=false
```
> Keep `.env` **out of Git**. Add it to `.gitignore`.  
> A public `.env.example` with placeholders is safe to commit.

---

## ▶️ How to Run Each Part (for now)

### 1) Streamlit UI
```powershell
# Windows (with venv activated)
python -m streamlit run bot.py
# or
python -m streamlit run bot_ui.py
```
> If it says “`streamlit` not recognized”, you’re not using the venv or it’s not installed. Run:
> `pip install streamlit` and use `python -m streamlit ...`.

### 2) Record Audio (Mic → WAV)
```powershell
python record_test.py
```
- Saves a WAV you can feed into `SpeechRecognition` as an offline file.

### 3) STT from WAV (example snippet)
```python
import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile("input.wav") as src:
    audio = r.record(src)
text = r.recognize_google(audio)  # or use Whisper/other backends
print(text)
```

### 4) TTS via ElevenLabs (planned)
- After setting `ELEVEN_API_KEY`, call the ElevenLabs SDK to synthesize reply audio.

---

## 🪲 Troubleshooting

- **`ModuleNotFoundError: No module named 'speech_recognition'`**  
  `pip install SpeechRecognition` (inside venv)

- **PyAudio install issues (Windows)**  
  Try: `pip install pyaudio==0.2.13 --only-binary=:all:`  
  If still failing, temporarily avoid live mic by recording to WAV and using `AudioFile`.

- **Streamlit import crash**  
  Make sure you **don’t** have a file named `streamlit.py` in your project. Rename it (e.g., `app_ui.py`) and delete `__pycache__`.

- **FFmpeg not found**  
  Ensure `ffmpeg -version` works in terminal. Add FFmpeg `/bin` to PATH (Windows).

- **Mic permissions (macOS)**  
  System Settings → Privacy & Security → Microphone → allow Terminal/VS Code.

---

## Preliminary Project Results

- **Running Model:** Using hosted APIs only (STT via `SpeechRecognition`, LLM via Groq, TTS via ElevenLabs). **Local on-device model:** **not done yet**.  
- **Weights Loaded:** No local weights (providers manage them). **Local weights load/management:** **not done yet**.  
- **Inference:** Modules tested **individually** (record → WAV, LLM reply in `bot.py`, TTS → `avatar_output.mp3`). **End-to-end chaining in one Streamlit app:** **not done yet**.  
- **Predictions/Outputs:**  
  - STT → transcript (via file path; live mic path depends on PyAudio) — **partial**  
  - LLM → text reply — **done**  
  - TTS → MP3 saved (`avatar_output.mp3`) — **done**  
- **Speed:** Latency measurements (STT / LLM / TTS / E2E) **not done yet**.  
- **Metrics Used:** WER (STT), latency, MOS-lite (TTS), UX measures — **not done yet**.

---

## Jetson Validation Summary ✅ (evidence-style)

- **Audio I/O:** Recorded **16kHz mono** WAV on Jetson via `arecord`; verified with `ffprobe`.  
- **Local STT:** Transcribed on-device using **Vosk** (CPU). Output captured as `TRANSCRIPT: ...`.  
- **LLM/TTS (Hybrid):** Sent transcript to **Groq** for response and generated speech via **ElevenLabs**; saved `avatar_output.mp3`.  
- **UI:** Launched **Streamlit** (`bot_ui.py`) on Jetson (`:8501`) and accessed over LAN.  
- **Latency (sample):** Logged per-stage times (STT / LLM / TTS / total) for a short clip.  
- **Camera:** Enumerated using `v4l2-ctl`; live preview verified. *(Object detection planned via YOLO/TensorRT.)*

> Artifacts to attach when submitting: `input.wav`, `avatar_output.mp3`, terminal screenshots (`arecord -l`, `v4l2-ctl --list-devices`, `ffmpeg -version`, `TRANSCRIPT: ...`, latency line), Streamlit page capture.

---

## Next step to do 🚀

### 1) Connect Everything (E2E pipeline) 🔗  
**Goal:** One-click flow inside Streamlit: **Record → STT → LLM → TTS → Play**  
**Design (theoretical):**  
- **Capture:** Browser mic or local mic → 16kHz mono WAV  
- **STT:** Transcribe with `SpeechRecognition` (file) now; later replace with Whisper API or local Whisper on Jetson  
- **LLM:** Send transcript to **Groq** (therapeutic/system prompt) → empathetic reply text  
- **TTS:** Convert reply to speech (start with **ElevenLabs**; later optional local **Piper TTS** for offline)  
- **UI/State:** Show transcript + model reply; keep simple chat history for context  
**Acceptance criteria:** Streamlit page runs start→finish without manual file hops; output MP3 plays inline.  
**Metrics (later):** STT WER (sample clips), latency per stage (STT/LLM/TTS), perceived naturalness (1–5).

---

### 2) Jetson Integration (theoretical design) 🤖🎛️  
**Why hybrid:** Jetson is ideal for edge audio + light STT, while LLM/TTS live in cloud initially.  
**Recommended split:**  
- **On Jetson (edge):**  
  - Audio capture (ALSA/PulseAudio) → WAV  
  - **Local STT**: *faster-whisper* (CUDA/FP16) on Xavier/Orin or **Vosk** (CPU) on Nano  
  - Streamlit UI (headless) to orchestrate flow  
- **In cloud:**  
  - **Groq LLM** (therapeutic responses)  
  - **ElevenLabs TTS** (natural voices) → optional **Piper TTS** for offline later  
**Model sizing guidance:** Nano → `faster-whisper` *tiny* (or Vosk). Xavier/Orin → *tiny/base* FP16 OK.  
**Audio constraints:** 16kHz mono; short 5–10s chunks for responsiveness.  
**Security:** Keep raw audio on edge; send only transcript to cloud if needed.  
**Acceptance criteria:** Jetson records → local STT → cloud LLM → TTS → plays audio on Jetson.

---

### 3) Avatar Creation (theoretical) 🗣️🧑‍🎨  
**Goal:** Friendly on-screen avatar that **speaks** TTS audio and **reacts** to mood.  
**MVP:** Static PNG/SVG avatar + **audio waveform** animation while playing MP3; subtitles show LLM reply.  
**Enhanced:** 2D talking-head (viseme-driven) with basic emotion states (happy/neutral/concerned) driven by transcript sentiment.  
**Offline-friendly:** Use **Piper TTS** phoneme timings to drive visemes when offline.  
**Acceptance criteria:** Avatar renders, animates during playback, captions match spoken text.

---

### 4) Jetson Object Detection (camera) 📷🟦  
**Goal:** Optional context-aware cues (e.g., detect person presence/objects) via Jetson camera input.  
**Design (theoretical):**  
- **Capture:** CSI or USB webcam using `v4l2`/GStreamer.  
- **Model:** TensorRT-optimized **YOLO** (e.g., YOLOv5n/YOLOv8n) or NVIDIA **DetectNet** sample.  
- **Pipeline:** Camera → inference (TensorRT) → bounding boxes → lightweight events to Streamlit (e.g., “person detected”) to adapt bot UX.  
- **Performance:** Use **n/nano** variants, FP16/INT8 for real-time; 640×480 on Nano.  
- **Security:** On-device inference; don’t transmit frames by default.  
**Acceptance criteria:** Live camera preview + labels at ≥10 FPS; events optionally alter prompts (“user present”, “distraction detected”).

---

## 🧭 Roadmap (Next Steps) 🛠️

- [ ] **Connect** `record_test.py` mic capture directly to SR (live transcription).  
- [ ] **Add LLM** call (Groq) to generate empathetic, context-aware replies.  
- [ ] **Add TTS** (ElevenLabs) to speak the LLM response.  
- [ ] **Single Streamlit app** that does: Record → Transcribe → Think → Speak.  
- [ ] **Jetson edge STT** (faster-whisper/Vosk) + optional **Jetson object detection**.  
- [ ] **Avatar** (waveform → viseme-driven mouth).  
- [ ] **Metrics pass** (WER, latency, MOS-lite).  
- [ ] **Dockerfile** / one-click launch for easier setup.  
- [ ] **Unit tests** for audio I/O and API gateways.

---

## 🏷️ Scripts & Commands (Quick Reference)

```powershell
# Activate venv (Windows)
.\.venv\Scripts\Activate.ps1

# Install core deps
pip install -r requirements.txt

# Run UI
python -m streamlit run bot.py

# Record mic test
python record_test.py
```

---

## 🤝 Contributing

- Open issues for bugs or feature requests.
- Keep PRs small and focused (UI, audio, STT, TTS, or LLM separately).
- Don’t commit secrets—use `.env`.

---

## 📄 License

Add your preferred license (MIT recommended for open projects).

---

## 🙏 Acknowledgements

- Streamlit team for the rapid UI framework  
- ElevenLabs for TTS  
- Groq for LLM infra  
- Open-source contributors of `SpeechRecognition`, `PyAudio`, `sounddevice`

---

**TL;DR:** Everything runs **separately** right now. The goal is to **connect** audio capture → STT → LLM → TTS into one Streamlit app, with Jetson edge STT + optional object detection and a speaking avatar. 💪✨
