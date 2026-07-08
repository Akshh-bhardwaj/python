# chatbot.py
"""
💖 DORA 3.0 — Emotion-Aware, Hinglish + English Chatbot
✨ Features:
- Understands feelings (sad, happy, angry, bored, etc.)
- Detects jokes (even in Hinglish like “ek joke suna”)
- Multilingual (English + Hindi)
- Interactive colorful chat UI
- Speaks only when you press “🔊 Speak Reply”
"""

import io
import os
import re
import random
import string
import datetime
import subprocess
import streamlit as st
import speech_recognition as sr

try:
    import wikipedia
except Exception:
    wikipedia = None

try:
    import qrcode
except Exception:
    qrcode = None


# -------------------------
# Voice Control
# -------------------------
_say_process = None
_last_joke = None


def speak_async(text, lang):
    """Speak using macOS 'say' (non-blocking)."""
    global _say_process
    stop_speaking()
    voices = {
        "en-IN": "Samantha",
        "hi-IN": "Lekha",
        "en-US": "Alex",
    }
    voice = voices.get(lang, "Samantha")
    try:
        _say_process = subprocess.Popen(["say", "-v", voice, text])
    except Exception as e:
        print("Speech error:", e)


def stop_speaking():
    global _say_process
    if _say_process and _say_process.poll() is None:
        _say_process.terminate()
        _say_process = None


# -------------------------
# Listen Voice
# -------------------------
def listen(lang):
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.info("🎙️ Listening... speak now!")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
        try:
            st.success("✅ Recognizing...")
            text = recognizer.recognize_google(audio, language=lang)
            return text.lower()
        except:
            return "Sorry, couldn't understand your voice."
    except:
        return "Microphone not available."


# -------------------------
# Helper Functions
# -------------------------
def tell_joke():
    global _last_joke
    jokes = [
        "🤣 Ek developer baar me gaya... aur bola — 'Mujhe ek strong exception chahiye!'",
        "😂 Computer ka favorite dance? — Disk-o!",
        "😆 Java developer ne apna job kyun chhoda? — Because he didn’t get arrays!",
        "😜 Ek bug bola — mujhe mat maaro yaar, mai feature ban jaunga!",
        "🤓 I changed my password to 'incorrect' so when I forget, it says 'Your password is incorrect!'"
    ]
    joke = random.choice([j for j in jokes if j != _last_joke])
    _last_joke = joke
    return joke


def respond_to_emotion(text):
    """Detect emotion and reply like a friend."""
    text = text.lower()
    if any(word in text for word in ["sad", "dukhi", "lonely", "cry", "depressed"]):
        return random.choice([
            "💖 Ohh... don’t be sad yaar. Life ups and downs hoti rehti hain. Smile zara 😄",
            "🥺 Aww, mujhe bhi bura lag raha hai... chale ek joke sunata hoon?",
            "🌈 Sab theek ho jaayega. You’re stronger than you think!"
        ])
    elif any(word in text for word in ["happy", "khush", "great", "awesome"]):
        return random.choice([
            "😄 Wahh! Ye to mast baat hai!",
            "💃 Keep shining yaar! Happiness suits you!",
            "🎉 Nice! Mujhe bhi khushi hui sunke!"
        ])
    elif any(word in text for word in ["angry", "gussa", "mad"]):
        return random.choice([
            "😤 Arre chill bro! Thoda sa paani pee lo 💧",
            "🧘 Deep breath le yaar... sab sahi ho jaayega.",
            "😅 Gussa kam karo, warna code crash ho jaayega!"
        ])
    elif any(word in text for word in ["bored", "boring", "thak", "tired"]):
        return random.choice([
            "😴 Bored ho kya? Chal ek joke sunata hoon!",
            "😂 Thoda relax kar yaar, life itni serious nahi!",
            "🎮 Chal koi game khelenge baad me?"
        ])
    else:
        return None


def quote_of_day():
    quotes = [
        "🌟 Believe in yourself!",
        "💪 Hard work beats talent!",
        "🔥 Push harder — your future self will thank you.",
        "🚀 Great things never come from comfort zones."
    ]
    return random.choice(quotes)


def handle_command(text):
    text = text.lower().strip()
    qr_bytes = None
    reply = ""

    # Emotion detection
    emotion_reply = respond_to_emotion(text)
    if emotion_reply:
        return {"reply": emotion_reply, "qr_bytes": qr_bytes}

    # Joke detection (English/Hindi)
    if any(word in text for word in ["joke", "majak", "sunao", "suna", "funny"]):
        return {"reply": tell_joke(), "qr_bytes": qr_bytes}

    if any(word in text for word in ["hello", "hi", "hey", "namaste"]):
        reply = "👋 Hello! Kaise ho? I’m DORA, your chat buddy!"
    elif "help" in text:
        reply = "💡 Try saying: 'ek joke suna', 'I am sad', 'calculate 2+2', or 'date'."
    elif "calc" in text or re.match(r'^[0-9+\-*/(). %]+$', text):
        try:
            val = eval(text.replace("calc", "").strip())
            reply = f"🧮 Result: {val}"
        except:
            reply = "❌ Sorry, expression samajh nahi aaya."
    elif "date" in text:
        now = datetime.datetime.now()
        reply = now.strftime("📅 Aaj ki date: %A, %d %B %Y — %I:%M %p")
    elif "quote" in text:
        reply = quote_of_day()
    else:
        reply = "🤔 Hmm... mujhe ye samajh nahi aaya, but you sound interesting! Tell me more?"

    return {"reply": reply, "qr_bytes": qr_bytes}


# -------------------------
# Streamlit Chat UI
# -------------------------
def run_chatbot():
    st.set_page_config(page_title="DORA 3.0", layout="centered")
    st.markdown(
        "<h1 style='text-align:center; color:#FF4081;'>🤖 DORA 3.0 — Your Emotional Chat Buddy 💬</h1>",
        unsafe_allow_html=True,
    )

    # Language setup
    if "language" not in st.session_state:
        st.session_state.language = None

    if not st.session_state.language:
        st.markdown("### 🌐 Choose your language to talk:")
        lang_map = {"English": "en-IN", "Hindi": "hi-IN"}
        lang_choice = st.radio("Select:", list(lang_map.keys()))
        if st.button("✅ Confirm Language"):
            st.session_state.language = lang_map[lang_choice]
            st.success(f"Language set to {lang_choice}! Now say something 😄")
            st.rerun()
        return

    lang_choice = st.session_state.language

    # Chat setup
    if "messages" not in st.session_state:
        st.session_state.messages = [("DORA", "Hey! Type or speak to start chatting 😄")]

    st.markdown("<div style='height:350px; overflow-y:auto; border:1px solid #ccc; padding:10px; border-radius:10px;'>", unsafe_allow_html=True)
    for who, msg in st.session_state.messages:
        if who == "You":
            st.markdown(f"<div style='text-align:right; background:#E3F2FD; padding:8px; border-radius:10px; margin:5px;'><b>{who}:</b> {msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align:left; background:#FCE4EC; padding:8px; border-radius:10px; margin:5px;'><b>{who}:</b> {msg}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    user_input = st.text_input("💬 Type here or press 🎙️ Speak")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("Send"):
            if user_input:
                st.session_state.messages.append(("You", user_input))
                out = handle_command(user_input)
                st.session_state.messages.append(("DORA", out["reply"]))
                st.session_state.last_reply = out["reply"]
                st.rerun()

    with col2:
        if st.button("🎙️ Speak"):
            voice_text = listen(lang_choice)
            st.session_state.messages.append(("You", voice_text))
            out = handle_command(voice_text)
            st.session_state.messages.append(("DORA", out["reply"]))
            st.session_state.last_reply = out["reply"]
            st.rerun()

    with col3:
        if st.button("🔊 Speak Reply"):
            if "last_reply" in st.session_state:
                speak_async(st.session_state.last_reply, lang_choice)

    with col4:
        if st.button("🛑 Stop"):
            stop_speaking()

    with col5:
        if st.button("🧹 Clear"):
            stop_speaking()
            st.session_state.messages = [("DORA", "Chat cleared. Ready to talk again 💖")]


if __name__ == "__main__":
    run_chatbot()
