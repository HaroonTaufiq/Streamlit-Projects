import streamlit as st
from transformers import VitsModel, AutoTokenizer, pipeline
import torch
import numpy as np
import io
import soundfile as sf
import PyPDF2

# Load models and tokenizers
tts_model = VitsModel.from_pretrained("facebook/mms-tts-eng")
tts_tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-eng")
sentiment_analysis_model = pipeline("sentiment-analysis")

def generate_speech(text, sampling_rate, pitch_shift=0):
    inputs = tts_tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        output = tts_model(**inputs).waveform

    waveform = output.squeeze().cpu().numpy()

    # Apply pitch shift (if any)
    if pitch_shift != 0:
        waveform = np.interp(waveform, (waveform.min(), waveform.max()), (-pitch_shift, pitch_shift))

    audio_bytes_io = io.BytesIO()
    sf.write(audio_bytes_io, waveform, samplerate=sampling_rate, format='WAV')
    audio_bytes_io.seek(0)

    return audio_bytes_io

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Streamlit UI
st.title("Hugging Face Model Application")
st.write("Choose a task")

# Task selection
task = st.selectbox("Select a task", ["Text-to-Speech", "Sentiment Analysis"])

# PDF upload option
pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

if task == "Text-to-Speech":
    st.write("Enter text or upload a PDF to convert it to speech.")
    if pdf_file:
        text_input = extract_text_from_pdf(pdf_file)
        st.text_area("Extracted Text", text_input, height=200)
    else:
        text_input = st.text_area("Text to convert:", "Some example text in the English language")
    
    # Customization options
    st.write("Customization Options")
    sampling_rate = st.selectbox("Sampling Rate", [22050, 44100], index=0)
    pitch_shift = st.slider("Pitch Shift", -10, 10, 0)

    if st.button("Generate Speech"):
        if text_input:
            st.write("Generating speech...")
            audio_bytes_io = generate_speech(text_input, sampling_rate, pitch_shift)
            st.audio(audio_bytes_io, format="audio/wav")
        else:
            st.write("Please enter some text or upload a PDF.")

elif task == "Sentiment Analysis":
    st.write("Enter text or upload a PDF to analyze sentiment.")
    if pdf_file:
        text_input = extract_text_from_pdf(pdf_file)
        st.text_area("Extracted Text", text_input, height=200)
    else:
        text_input = st.text_area("Text to analyze:", "I love using Streamlit and Hugging Face models!")

    if st.button("Analyze Sentiment"):
        if text_input:
            st.write("Analyzing sentiment...")
            sentiment = sentiment_analysis_model(text_input)
            st.write("Sentiment:", sentiment)
        else:
            st.write("Please enter some text or upload a PDF.")