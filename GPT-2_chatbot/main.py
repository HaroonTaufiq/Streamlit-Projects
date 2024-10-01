import streamlit as st
from langchain.llms import HuggingFaceHub
import os

hf_token = os.getenv("HF_TOKEN")
  
# initialize hugging face model
repo_id = "openai-community/gpt2"
llm = HuggingFaceHub(
    repo_id=repo_id,
    huggingfacehub_api_token=hf_token,
    model_kwargs={"max_length": 128, "temperature": 0.7},
)

# Streamlit interface
st.title("GPT-2 Chatbot")
st.write("Type your message below and press Enter to send.")

user_input = st.text_input("You:")

if st.button("send"):
    if user_input:
        try:
            response = llm(user_input)
            st.write(f"Bot: {response}")
        except Exception as e:
            st.write("Error:", {str(e)})
else:
    st.write("Please enter your message.")
