import google.generativeai as genai
import os
import streamlit as st

# API config
API_KEY=os.environ["API_KEY"]
genai.configure(api_key=API_KEY)

# model initialization
model = genai.GenerativeModel("gemini-1.5-flash")

# User Prompting
# ------------------------------------- #
# response = model.generate_content("Write a story about a magic backpack.")
# print(response.text)
# ------------------------------------- #
# Function to get response from the model
def getResponsefromModel(User_prompt):
    response = model.generate_content(User_prompt)
    return response.text

# Streamlit app configuration
st.set_page_config(layout="centered")
st.title("Gemini Chatbot")
st.markdown("This is a chatbot that can generate text based on the input prompt using gemini-1.5-flash model.")

# Initialize history in session state if it doesn't exist
if "history" not in st.session_state:
    st.session_state["history"] = []

# CSS for styling
st.markdown("""
    <style>
    .chat-container {
        max-width: 700px;
        margin: 20px auto;
        padding: 20px;
        border-radius: 10px;
        background-color: #d1d3e0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        overflow-y: auto;
        max-height: 500px;
    }
    .chat-prompt {
        font-weight: bold;
        color: #00529B;
        margin-bottom: 5px;
    }
    .chat-response {
        background-color: grey;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 20px;
        color: #333;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .chat-message {
        margin-bottom: 15px;
        background-color: grey;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stTextInput input {
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
        width: 100%;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    .stButton button {
        background-color: #0073e6;
        color: black;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton button:hover {
        background-color: #005bb5;
    }
    </style>
    """, unsafe_allow_html=True)

# User Prompting 
# ------------------------------------- #
# on terminal
# User_prompt = input('Enter your prompt: ')
# getResponsefromModel(User_prompt)

# respond = getResponsefromModel(User_prompt)
# print(respond)

# ------------------------------------- #
# On streamlit
with st.form(key='chat_form', clear_on_submit=True):
    user_prompt = st.text_input("Enter your prompt:", max_chars=1000, label_visibility="collapsed")
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_prompt:
            respond = getResponsefromModel(user_prompt)
            st.session_state.history.append({"user": user_prompt, "model": respond})
        else:
            st.warning("Write a prompt first.")
   
# Display chat history
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
st.markdown("### Chat History")
for chat in st.session_state.history:
    st.markdown(f"<div class='chat-message'><div class='chat-prompt'>**Prompt:** {chat['user']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='chat-response'>**Response:** {chat['model']}</div></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
