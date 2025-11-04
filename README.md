# EmoCare Therapy Bot 🧠💬🎧

> **Status:** Components are currently **not connected**. Each file works **separately**.  
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
├─ Bot.py                      # Streamlit app (primary UI)
├─ Yipeeeee.py                 # Alternate Streamlit prototype (exported notebook)
├─ streamlit.ipynb             # Notebook used to design UI
├─ record_test.py              # Mic → WAV recorder & playback test
├─ Voice_Recorder_Setup...     # (if present) extra recording helpers / scripts
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
- **STT (Speech-to-Text):** `SpeechRecognition` (mic or WAV) 🗣️→📝  
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
python -m streamlit run Bot.py
# or
python -m streamlit run Yipeeeee.py
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

## 🧭 Roadmap (Next Steps) 🛠️

- [ ] **Connect** `record_test.py` mic capture directly to SR (live transcription).  
- [ ] **Add LLM** call (Groq) to generate empathetic, context-aware replies.  
- [ ] **Add TTS** (ElevenLabs) to speak the LLM response.  
- [ ] **Single Streamlit app** that does: Record → Transcribe → Think → Speak.  
- [ ] **Emotion detection** (rule-based / model-based) to tailor responses.  
- [ ] **Session history** + simple prompt engineering for continuity.  
- [ ] **Dockerfile** / one-click launch for easier setup.  
- [ ] **Unit tests** for audio I/O and API gateways.

---

## 🧪 Suggested Integration Flow

1. **Record** audio in Streamlit (web mic) or via `sounddevice`.  
2. **SR**: Transcribe with `SpeechRecognition` (or Whisper API).  
3. **LLM**: Send transcript to Groq (system prompt = therapist style).  
4. **TTS**: Convert model reply to audio with ElevenLabs.  
5. **UI**: Display transcript + play audio response; keep chat history.

---

## 🏷️ Scripts & Commands (Quick Reference)

```powershell
# Activate venv (Windows)
.\.venv\Scripts\Activate.ps1

# Install core deps
pip install -r requirements.txt

# Run UI
python -m streamlit run Bot.py

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

**TL;DR:** Everything runs **separately** right now. The goal is to **connect** audio capture → STT → LLM → TTS into one Streamlit app. 💪✨
