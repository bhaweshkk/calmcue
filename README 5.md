CalmCue

CalmCue is a simple, offline-friendly emotional first-aid tool built with Python and Streamlit. It is designed for moments when you feel anxious, overwhelmed, sad, lonely, unmotivated, or mentally foggy and need a quick moment of relief.

CalmCue is **not** a chatbot, **not** a therapy app, and **not** a journaling app. It is a lightweight tool that gives you:

1. A short supportive message
2. A breathing or grounding exercise
3. One small, practical next action
4. Optional "Read Aloud" audio for the response

Important Disclaimer

CalmCue does **not** diagnose any mental health condition and is **not** a replacement for therapy, counseling, or medical care. If you are in crisis, please contact a trusted person or your local emergency/helpline services immediately. (See the in-app crisis message for more.)

Project Structure

```
CalmCue/
├── app.py              # Main Streamlit app (UI)
├── helpers.py          # Emotion detection, crisis check, text-to-speech
├── data.py              # All response content (messages, exercises, actions)
├── requirements.txt     # Python dependencies
└── README.md             # This file
```

About the "Read Aloud" Feature

CalmCue uses **gTTS (Google Text-to-Speech)** to convert responses into audio.

**Why gTTS instead of pyttsx3?** pyttsx3 relies on Windows' built-in voice engine, which can behave inconsistently across different Windows versions and sometimes freezes or throws driver errors. gTTS is more stable and predictable, though it does require an active internet connection to generate audio. If you're offline, the text response will still display normally — only the audio button will show a friendly message instead.

Future Improvement Ideas

1. **Multi-language support** — let users type and receive responses in their native language for wider accessibility.
2. **Local audio files instead of gTTS** — pre-record calming audio clips so Read Aloud works fully offline.
3. **Breathing animation** — a simple animated circle that expands and contracts in sync with the breathing exercise timing.
4. **Mood trend view** — using only session state (no database), show a simple chart of emotions detected during the current session.
5. **Improved keyword detection** — expand keyword lists or introduce simple scoring weights so subtle phrasing is detected more accurately.

CalmCue was built to be small, simple, and immediately useful — a gentle pause button, not a diagnostic tool. If it helps even one person take one calming breath, it's done its job.
