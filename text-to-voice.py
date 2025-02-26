import streamlit as st
import pyttsx3
import tempfile
import os

# Streamlit App Configuration
st.set_page_config(page_title="Text to Voice Converter", page_icon="🔊", layout="wide")

# Custom CSS for colorful UI
st.markdown(
    """
    <style>
        body {background-color: #f0f8ff;}
        .stApp {background: linear-gradient(to right, #ff9a9e, #fad0c4);}
        .title {color: white; text-align: center; font-size: 36px;}
        .subtitle {color: white; text-align: center; font-size: 20px;}
        .stButton>button {background-color: #ff5722; color: white; border-radius: 8px;}
        .stTextArea textarea {background-color: #ffffff; color: #333; border-radius: 8px;}
        .stRadio label {color: white;}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='title'>🔊 Text to Voice Converter</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subtitle'>Enter your text and convert it into speech.</h3>", unsafe_allow_html=True)

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Voice Selection
voice_options = ["Male", "Female"]
selected_voice = st.radio("Select Voice Type", voice_options)

if selected_voice == "Male":
    engine.setProperty('voice', voices[0].id)
else:
    engine.setProperty('voice', voices[1].id)

# Input Text
text_input = st.text_area("Enter text to convert into speech:")

if st.button("🎙 Convert to Voice"):
    if text_input:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            temp_path = temp_audio.name
        
        engine.save_to_file(text_input, temp_path)
        engine.runAndWait()
        
        st.audio(temp_path, format='audio/mp3')
        
        st.download_button("📥 Download Audio", open(temp_path, "rb"), file_name="text_to_speech.mp3", mime="audio/mp3")
        
        os.remove(temp_path)
    else:
        st.warning("Please enter some text to convert!")

st.markdown("🔹 **Create by Ammar Ahmed**")
