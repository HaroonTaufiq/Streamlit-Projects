#  pip install streamlit transformers torch numpy soundfile PyPDF2
'''
1. Customization Options
We'll add options for adjusting the speech rate and pitch, and allow users to select a different sampling rate if needed.

2. PDF Support
We'll use the PyPDF2 library to extract text from PDF files and convert it into speech.

'''

import streamlit as st
from transformers import VitsModel, AutoTokenizer
import torch
import numpy as np
import io
import soundfile as sf
import PyPDF2

# Load model and tokenizer
model = VitsModel.from_pretrained("facebook/mms-tts-eng")
tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-eng")

def generate_speech(text, sampling_rate, pitch_shift=0):
    inputs = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        output = model(**inputs).waveform

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
st.title("Text-to-Speech Converter")
st.write("Enter text or upload a PDF to convert it to speech.")

# PDF upload option
pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

# Text input
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

        # Display audio in Streamlit
        st.audio(audio_bytes_io, format="audio/wav")
    else:
        st.write("Please enter some text or upload a PDF.")