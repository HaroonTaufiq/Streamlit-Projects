# Streamlit app for Palm-RAG-QA-chatbot
import streamlit as st

# Import the necessary functions from langchain_helper.py
from langchain_helper import get_qa_chain, create_vector_db 

st.title("Palm-RAG-QA-chatbot for Udemy course.")

question = st.text_input("Enter your question here:")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Answer:")
    st.write(response["result"])