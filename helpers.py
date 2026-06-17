import io
from data import EMOTION_KEYWORDS, CRISIS_KEYWORDS
def check_for_crisis(user_text: str) -> bool:
    """
    Checks if the user's text contains any crisis-related phrases.

    Parameters:
        user_text (str): the raw text typed by the user

    Returns:
        bool: True if a crisis phrase is found, False otherwise
    """

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
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)

        return audio_buffer.read()

    except Exception:
        return None
