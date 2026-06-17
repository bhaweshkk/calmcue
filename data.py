EMOTION_KEYWORDS = {
    "anxiety": [
        "anxious", "anxiety", "nervous", "panic", "worried", "worry",
        "scared", "afraid", "on edge", "racing heart", "tense"
    ],
    "overwhelm": [
        "overwhelmed", "overwhelm", "too much", "can't cope", "cannot cope",
        "drowning", "burnt out", "burned out", "exhausted", "too many things"
    ],
    "sadness": [
        "sad", "sadness", "down", "unhappy", "hurt", "crying", "cry",
        "heartbroken", "low", "depressed", "feel like giving up"
    ],
    "loneliness": [
        "lonely", "loneliness", "alone", "isolated", "no one understands",
        "nobody cares", "left out", "disconnected"
    ],
    "low_motivation": [
        "no motivation", "unmotivated", "lazy", "can't start", "cannot start",
        "procrastinating", "procrastinate", "stuck", "no energy", "tired of trying"
    ],
    "confusion": [
        "confused", "confusion", "overthinking", "can't focus", "cannot focus",
        "can't think", "cannot think", "lost", "don't know what to do",
        "do not know what to do", "unclear", "foggy"
    ],
}
CRISIS_KEYWORDS = [
    "want to die",
    "want to kill myself",
    "kill myself",
    "want to harm myself",
    "harm myself",
    "want to end my life",
    "end my life",
    "end it all",
    "no reason to live",
    "better off dead",
    "suicide",
    "suicidal",
]
EMOTION_DATA = {
    "anxiety": {
        "label": "Anxiety",
        "message": (
            "It's okay to feel anxious right now. Your feelings are valid, "
            "and this feeling will pass. You are safe in this moment."
        ),
        "exercise": (
            "Try this: Breathe in slowly for 4 seconds, hold for 4 seconds, "
            "then breathe out slowly for 6 seconds. Repeat this 3 times."
        ),
        "action": (
            "Small action: Unclench your jaw and drop your shoulders. "
            "Take one sip of water."
        ),
    },
    "overwhelm": {
        "label": "Overwhelm",
        "message": (
            "It sounds like a lot is piling up right now. You don't have to "
            "handle everything at once. One step at a time is enough."
        ),
        "exercise": (
            "Try this: Name 3 things you can see, 2 things you can hear, "
            "and 1 thing you can feel right now. This brings you back to the present."
        ),
        "action": (
            "Small action: Write down just ONE task you'll do next. Ignore the rest for now."
        ),
    },
    "sadness": {
        "label": "Sadness",
        "message": (
            "It's okay to feel sad. You don't need a reason to feel this way, "
            "and you don't have to pretend you're okay right now."
        ),
        "exercise": (
            "Try this: Place a hand on your chest, breathe slowly, and say to "
            "yourself, 'This feeling is temporary.'"
        ),
        "action": (
            "Small action: Send a short message to someone you trust, even just to say hi."
        ),
    },
    "loneliness": {
        "label": "Loneliness",
        "message": (
            "Feeling alone is really hard, and your feelings matter even if "
            "no one else is around right now. You are not as alone as it feels."
        ),
        "exercise": (
            "Try this: Take 5 slow breaths and gently remind yourself, "
            "'This moment will pass.'"
        ),
        "action": (
            "Small action: Reach out to one person today, even with a short, simple message."
        ),
    },
    "low_motivation": {
        "label": "Low Motivation",
        "message": (
            "It's okay to not feel motivated right now. You don't have to be "
            "productive to be worthy of rest."
        ),
        "exercise": (
            "Try this: Sit up straight, take 3 deep breaths, and stretch your arms above your head."
        ),
        "action": (
            "Small action: Do just ONE tiny task for 2 minutes. That's enough for now."
        ),
    },
    "confusion": {
        "label": "Confusion",
        "message": (
            "It's okay to feel mentally foggy right now. You don't need to "
            "figure everything out immediately."
        ),
        "exercise": (
            "Try this: Close your eyes, breathe in for 4 seconds, breathe out for 4 seconds, "
            "and let your thoughts slow down."
        ),
        "action": (
            "Small action: Write down whatever is on your mind in one short, messy sentence. "
            "No need to make it neat."
        ),
    },
    "fallback": {
        "label": "General Support",
        "message": (
            "Thank you for sharing how you feel. Whatever you're experiencing right now, "
            "it's okay, and it's valid."
        ),
        "exercise": (
            "Try this: Take a slow breath in for 4 seconds, hold for 4 seconds, "
            "and breathe out for 4 seconds."
        ),
        "action": (
            "Small action: Pause for 10 seconds and just notice your breathing, without changing it."
        ),
    },
}
CRISIS_RESPONSE = {
    "label": "Urgent Support Needed",
    "message": (
        "It sounds like you are going through something very serious and painful right now. "
        "You do not have to face this alone, and your life matters."
    ),
    "instruction": (
        "Please reach out to a trusted person right now \u2014 a family member, friend, "
        "teacher, or counselor \u2014 and let them know how you're feeling. "
        "If you are in immediate danger, please contact local emergency services right away."
    ),
    "helpline_placeholder": (
        "Placeholder Helpline (replace with your local helpline): "
        "National Helpline: XXX-XXX-XXXX | Available 24/7"
    ),
}
