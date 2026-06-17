# helpers.py
# -----------------------------------------------------------------------------
# This file contains the "thinking" functions for CalmCue:
#   1. check_for_crisis()   -> checks if the text contains dangerous phrases
#   2. detect_emotion()     -> figures out which emotion category fits best
#   3. text_to_speech_bytes() -> converts text into audio (for Read Aloud)
#
# Beginner note: keeping these functions separate from app.py means the
# "logic" and the "screen" don't get tangled together. This makes the code
# easier to read and easier to fix if something goes wrong.
# -----------------------------------------------------------------------------

import io
from data import EMOTION_KEYWORDS, CRISIS_KEYWORDS

# We import gTTS inside the function (not at the top) so that if it's ever
# missing or fails for some reason, the rest of the app still works fine
# (Read Aloud will simply show an error message instead of crashing the app).


def check_for_crisis(user_text: str) -> bool:
    """
    Checks if the user's text contains any crisis-related phrases.

    Parameters:
        user_text (str): the raw text typed by the user

    Returns:
        bool: True if a crisis phrase is found, False otherwise
    """
    # Convert to lowercase so detection works no matter how the user typed it
    text_lower = user_text.lower()

    for phrase in CRISIS_KEYWORDS:
        if phrase in text_lower:
            return True

    return False


def detect_emotion(user_text: str) -> str:
    """
    Looks at the user's text and matches it against keyword lists
    to figure out which emotional category fits best.

    Parameters:
        user_text (str): the raw text typed by the user

    Returns:
        str: the name of the matched emotion category,
             or "fallback" if nothing matches.
    """
    text_lower = user_text.lower()

    # We count how many keywords match for each category, then pick the
    # category with the most matches. This is simple "rule-based" logic,
    # no machine learning needed.
    best_category = "fallback"
    best_score = 0

    for category, keywords in EMOTION_KEYWORDS.items():
        score = 0
        for keyword in keywords:
            if keyword in text_lower:
                score += 1

        if score > best_score:
            best_score = score
            best_category = category

    return best_category


def text_to_speech_bytes(text: str):
    """
    Converts the given text into speech audio using gTTS (Google Text-to-Speech).

    Why gTTS instead of pyttsx3?
    - pyttsx3 relies on the operating system's built-in voice engine (SAPI5
      on Windows). This can behave inconsistently across different Windows
      versions, sometimes causing the app to freeze or throw driver errors.
    - gTTS simply generates an MP3 file in memory and needs internet access,
      but it is far more stable and beginner-friendly, with fewer setup
      headaches on Windows.
    - Since CalmCue is meant to "minimize setup errors", gTTS is the safer
      default choice for Version 1.

    Parameters:
        text (str): the text to convert into speech

    Returns:
        bytes or None: MP3 audio data if successful, or None if it fails
    """
    try:
        from gtts import gTTS

        tts = gTTS(text=text, lang="en")

        # Save audio into memory (no temporary file needed on disk)
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)

        return audio_buffer.read()

    except Exception:
        # If anything goes wrong (e.g. no internet connection),
        # we return None so app.py can show a friendly error instead
        # of crashing the whole app.
        return None
