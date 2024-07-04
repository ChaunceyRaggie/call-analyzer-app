import streamlit as st
import whisper
import os
import pydantic
from langchain.llms import Ollama
from get_summary import get_call_summary


st.title("Call Detail Extractor")

# Set the path to the FFmpeg executable
ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe" 
os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)

# upload audio file with streamlit
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])

model = whisper.load_model("base")
st.text("Whisper Model Loaded")


if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing Audio")
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success("Transcription Complete")
        st.markdown(transcription["text"])
        summary = get_call_summary(transcription["text"])
        st.write(summary)
    else:
        st.sidebar.error("Please upload an audio file")


st.sidebar.header("Play Original Audio File")
st.sidebar.audio(audio_file)

