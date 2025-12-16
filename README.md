🧠 EmoCare: AI Wellness Companion 🧘🏻‍♀️
An AI-powered, empathetic conversational agent built to provide gentle support and self-reflection space.

Status
Course & Context
Framework
Complete ✅

Data 690: Special Topics in AI
Streamlit, Groq, ElevenLabs

✨ Overview
EmoCare is more than a chatbot; it's a personalized wellness companion designed to help users process their emotions, find healthy coping strategies, and track their reflections in a gentle, non-judgmental environment.

This project was developed as part of my Data 690: Special Topics in AI course, under the guidance of Prof. Levan Sulimanov.

🚀 Key Features
Custom Theming: A unique, warm, and minimal aesthetic using Streamlit's custom CSS (wellness.css) for a cozy user experience.

Conversational AI: Utilizes Groq's high-speed API (via Llama 3.1) for fast, empathetic, and context-aware responses based on the user's chosen mood and focus area.

Voice Mode (🎙️ STT & 🔊 TTS): Seamless integration with ElevenLabs for Speech-to-Text (STT) transcription and Text-to-Speech (TTS) voice responses, making interaction hands-free and more personal.

Personalized Context: Users can upload a personal journal/notes PDF for EmoCare to use as context, along with an auto-generated Word Cloud for visual insights.

Action Compass: A dynamic sidebar component that provides immediate, gentle, mood-based action nudges (e.g., "Angry → Sing it out 🎵").

Calm Quest Mini-Game: A 3-step, 60-second guided reset for grounding, including a breathing timer, a focus exercise, and a one-line journaling prompt.

Mood-based Music: Recommendations for relevant YouTube playlists based on the user's selected mood.

🛠️ Installation and Setup
1. Clone the Repository
Bash
git clone <your-repo-link>
cd emacare

2. Install Dependencies
All required packages are listed in requirements.txt
Bash
pip install -r requirements.txt

(Note: This requires ffmpeg to be installed on your system for ffmpeg-python.)

3. Configure Environment Variables
Create a file named .env in the root directory and populate it with your API keys:

GROQ_API_KEY=gsk_...
ELEVENLABS_API_KEY=sk_...

GROQ_API_KEY: Required for the core conversational logic (LLM).
ELEVENLABS_API_KEY: Required for Voice Mode (STT) and Text-to-Speech (TTS).

4. Run the Application
Bash
streamlit run wellness.py

🐛 Troubleshooting and Solutions
Developing EmoCare required overcoming a few key technical hurdles, particularly around the real-time audio components.

Problem Encountered
Solution & Fix

ElevenLabs TTS Output Stream
The ElevenLabs SDK could return audio data as either a bytes object or an iterable stream. The fix was to check the return type and use b"".join(chunk for chunk in audio_result) to correctly combine chunks if a generator was returned.

ElevenLabs STT Model ID
Initial attempts at Speech-to-Text failed with generic model IDs. The critical fix was identifying and explicitly using the correct STT model ID, "scribe_v1", which is optimized for transcription.

sounddevice Device Selection
Handling local audio devices (sounddevice) in Streamlit required saving the device IDs in st.session_state and explicitly setting sd.default.device as a tuple (input_device_id, output_device_id) when the user clicked "Apply Devices".

Streamlit st.button Reruns
The nature of Streamlit's state management meant actions like "Record Voice" or "Start Breathing" required an immediate state update and a hard st.rerun() to reflect changes and transition the UI steps.

🖼️ User Interface & Response Examples
EmoCare Response Example:

User Input: (Voice)
"I feel like I have too much on my plate this week. My boss gave me two huge deadlines and I haven't slept well."

Companion:
"That sounds like a heavy load to carry right now. It's completely understandable that you're feeling overwhelmed and losing sleep. Remember, your worth isn't tied to your productivity. Could you try one small act of self-care right now, like stepping away from your desk for 90 seconds and stretching? And, when you look at your calendar, is there one meeting you could postpone or one small task you could delegate to give yourself a tiny bit more room to breathe?"

Action Compass Example:
A user selects Stressed / Overwhelmed as their current mood. The Action Compass automatically highlights a suggestion:

<div class="compass-swatch active"><b>Stressed</b> → 🏃 Move your body – even 60 seconds counts</div>

🙏 Acknowledgements
Prof. Levan Sulimanov: For providing the framework and inspiration within the Data 690 course to explore advanced AI applications in the realm of mental wellness.

Groq: For providing blazing-fast LLM inference that makes the conversational experience feel immediate and supportive.

ElevenLabs: For the high-quality, seamless Speech-to-Text and Text-to-Speech APIs that brought the companion to life.

Streamlit: For the incredible open-source platform that made it possible to build a professional-grade web application entirely in Python.
