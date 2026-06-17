# app.py
# -----------------------------------------------------------------------------
# CalmCue - Main Application File
#
# This is the file you run with: streamlit run app.py
#
# This file controls everything the user SEES and CLICKS.
# All the "thinking" (emotion detection, crisis check, text-to-speech)
# happens in helpers.py. All the content (messages, exercises, actions)
# lives in data.py.
# -----------------------------------------------------------------------------

import streamlit as st
from data import EMOTION_DATA, CRISIS_RESPONSE
from helpers import check_for_crisis, detect_emotion, text_to_speech_bytes


# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="CalmCue",
    page_icon="🌿",
    layout="centered",
)

# -----------------------------------------------------------------------------
# SIMPLE CUSTOM STYLING
# A little bit of CSS to make the app feel calm and soft.
# This is optional but improves the experience for stressed users.
# -----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F4F8F7;
    }
    div.stButton > button {
        background-color: #A8D5BA;
        color: #1B3B2F;
        border-radius: 12px;
        border: none;
        padding: 0.6em 1.2em;
        font-size: 18px;
        font-weight: 600;
    }
    div.stButton > button:hover {
        background-color: #8FC4A4;
        color: #1B3B2F;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# SESSION STATE SETUP
# Streamlit re-runs the whole script every time the user clicks something,
# so we use "session_state" to remember information between those re-runs.
# This is NOT a database - it only lives while the browser tab is open.
# -----------------------------------------------------------------------------
if "result_category" not in st.session_state:
    st.session_state.result_category = None

if "is_crisis" not in st.session_state:
    st.session_state.is_crisis = False

if "history" not in st.session_state:
    # Optional small feature: remember past entries during this session only
    st.session_state.history = []


def reset_app():
    """Resets the app back to the starting state."""
    st.session_state.result_category = None
    st.session_state.is_crisis = False


# -----------------------------------------------------------------------------
# HOME / HEADER SECTION
# -----------------------------------------------------------------------------
st.markdown("<h1 style='text-align: center;'>🌿 CalmCue</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 18px;'>"
    "A quiet space for a moment of relief. Type how you feel, and CalmCue will "
    "offer a short message, a grounding exercise, and one small next step."
    "</p>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; font-size: 14px; color: #555;'>"
    "CalmCue is not a therapist and does not diagnose mental health conditions. "
    "It is a simple tool for immediate, gentle support."
    "</p>",
    unsafe_allow_html=True,
)

st.divider()

# -----------------------------------------------------------------------------
# INPUT SECTION
# -----------------------------------------------------------------------------
user_text = st.text_area(
    "How are you feeling right now?",
    placeholder="Example: I feel anxious about my exam tomorrow...",
    height=120,
)

col1, col2 = st.columns(2)

with col1:
    submit_clicked = st.button("💬 Get Support", use_container_width=True)

with col2:
    reset_clicked = st.button("🔄 Try Again", use_container_width=True)

if reset_clicked:
    reset_app()
    st.rerun()

# -----------------------------------------------------------------------------
# PROCESS INPUT
# -----------------------------------------------------------------------------
if submit_clicked:
    if not user_text or user_text.strip() == "":
        st.warning("Please type how you're feeling before continuing.")
    else:
        # STEP 1: Always check for crisis language FIRST, before anything else.
        if check_for_crisis(user_text):
            st.session_state.is_crisis = True
            st.session_state.result_category = None
        else:
            st.session_state.is_crisis = False
            category = detect_emotion(user_text)
            st.session_state.result_category = category

            # Optional: save to session-only history (not a database)
            st.session_state.history.append(
                {"text": user_text, "category": category}
            )

# -----------------------------------------------------------------------------
# DISPLAY: CRISIS RESPONSE (highest priority)
# -----------------------------------------------------------------------------
if st.session_state.is_crisis:
    st.error(f"### {CRISIS_RESPONSE['label']}")
    st.markdown(f"**{CRISIS_RESPONSE['message']}**")
    st.markdown(CRISIS_RESPONSE["instruction"])
    st.info(CRISIS_RESPONSE["helpline_placeholder"])
    st.markdown(
        "<p style='font-size:14px; color:#555;'>"
        "CalmCue is not equipped to handle crisis situations. Please contact "
        "a real person or emergency service right away."
        "</p>",
        unsafe_allow_html=True,
    )

# -----------------------------------------------------------------------------
# DISPLAY: NORMAL SUPPORT RESPONSE
# -----------------------------------------------------------------------------
elif st.session_state.result_category is not None:
    category = st.session_state.result_category
    content = EMOTION_DATA[category]

    st.subheader(f"💚 {content['label']}")

    st.markdown(f"**Message:** {content['message']}")
    st.markdown(f"**Grounding step:** {content['exercise']}")
    st.markdown(f"**Small action:** {content['action']}")

    st.markdown("")  # small spacing

    # Read Aloud button
    if st.button("🔊 Read Aloud"):
        full_text = f"{content['message']} {content['exercise']} {content['action']}"
        with st.spinner("Generating audio..."):
            audio_data = text_to_speech_bytes(full_text)

        if audio_data:
            st.audio(audio_data, format="audio/mp3")
        else:
            st.warning(
                "Sorry, audio could not be generated right now. "
                "This usually means there is no internet connection available. "
                "The text response above is still fully available."
            )

st.divider()
st.markdown(
    "<p style='text-align: center; font-size: 12px; color: #888;'>"
    "CalmCue \u2014 a simple offline-first emotional support tool. "
    "Not a substitute for professional help."
    "</p>",
    unsafe_allow_html=True,
)
