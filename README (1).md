# 🌿 CalmCue

CalmCue is a simple, offline-friendly emotional first-aid tool built with Python and Streamlit. It is designed for moments when you feel anxious, overwhelmed, sad, lonely, unmotivated, or mentally foggy and need a quick moment of relief.

CalmCue is **not** a chatbot, **not** a therapy app, and **not** a journaling app. It is a lightweight tool that gives you:

1. A short supportive message
2. A breathing or grounding exercise
3. One small, practical next action
4. Optional "Read Aloud" audio for the response

---

## ⚠️ Important Disclaimer

CalmCue does **not** diagnose any mental health condition and is **not** a replacement for therapy, counseling, or medical care. If you are in crisis, please contact a trusted person or your local emergency/helpline services immediately. (See the in-app crisis message for more.)

---

## 📁 Project Structure

```
CalmCue/
├── app.py              # Main Streamlit app (UI)
├── helpers.py          # Emotion detection, crisis check, text-to-speech
├── data.py              # All response content (messages, exercises, actions)
├── requirements.txt     # Python dependencies
└── README.md             # This file
```

---

## 🪟 How to Run on Windows (Step by Step)

### Step 1 — Install Python
If you don't already have Python installed, download it from [python.org/downloads](https://www.python.org/downloads/). During installation, make sure to check the box that says **"Add Python to PATH"**.

### Step 2 — Download/Copy the Project
Place the `CalmCue` folder anywhere on your computer, for example:
```
C:\Users\YourName\Desktop\CalmCue
```

### Step 3 — Open Command Prompt in the Project Folder
- Open the `CalmCue` folder in File Explorer
- Click on the address bar, type `cmd`, and press Enter
  (This opens Command Prompt directly inside the folder)

### Step 4 — Create a Virtual Environment (Recommended)
This keeps CalmCue's packages separate from other Python projects.
```
python -m venv venv
venv\Scripts\activate
```
You should see `(venv)` appear at the start of your command line.

### Step 5 — Install Dependencies
```
pip install -r requirements.txt
```

### Step 6 — Run the App
```
streamlit run app.py
```

### Step 7 — Open in Browser
Streamlit will automatically open a browser tab. If it doesn't, copy the **Local URL** shown in the terminal (usually `http://localhost:8501`) and paste it into your browser.

### Step 8 — Stop the App
Go back to the Command Prompt window and press `Ctrl + C`.

---

## 🔊 About the "Read Aloud" Feature

CalmCue uses **gTTS (Google Text-to-Speech)** to convert responses into audio.

**Why gTTS instead of pyttsx3?** pyttsx3 relies on Windows' built-in voice engine, which can behave inconsistently across different Windows versions and sometimes freezes or throws driver errors. gTTS is more stable and predictable, though it does require an active internet connection to generate audio. If you're offline, the text response will still display normally — only the audio button will show a friendly message instead.

---

## 🛠️ Common Errors & How to Fix Them

**1. `'streamlit' is not recognized as an internal or external command`**
This means Streamlit isn't installed or your virtual environment isn't activated. Run `venv\Scripts\activate` first, then `pip install -r requirements.txt` again.

**2. `ModuleNotFoundError: No module named 'gtts'`**
Run `pip install -r requirements.txt` again to make sure all packages installed correctly.

**3. Read Aloud button shows a warning instead of audio**
This usually means there's no internet connection. gTTS needs internet to generate speech. The text response is still fully visible above the button.

**4. The browser doesn't open automatically**
Manually copy the **Local URL** from the terminal (e.g., `http://localhost:8501`) and paste it into your browser.

**5. `pip` is not recognized**
This usually means Python wasn't added to PATH during installation. Reinstall Python and make sure to check "Add Python to PATH" during setup.

**6. Port already in use**
If another Streamlit app is already running, run this instead:
```
streamlit run app.py --server.port 8502
```

---

## 🚀 Future Improvement Ideas

1. **Multi-language support** — let users type and receive responses in their native language for wider accessibility.
2. **Local audio files instead of gTTS** — pre-record calming audio clips so Read Aloud works fully offline.
3. **Breathing animation** — a simple animated circle that expands and contracts in sync with the breathing exercise timing.
4. **Mood trend view** — using only session state (no database), show a simple chart of emotions detected during the current session.
5. **Improved keyword detection** — expand keyword lists or introduce simple scoring weights so subtle phrasing is detected more accurately.

---

## 💚 A Note on Purpose

CalmCue was built to be small, simple, and immediately useful — a gentle pause button, not a diagnostic tool. If it helps even one person take one calming breath, it's done its job.
