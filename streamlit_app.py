# streamlit_app.py

import streamlit as st
from chatbot import chatbot_response

# Configure page
st.set_page_config(page_title="EchoVerse Chatbot", page_icon="🎧")

st.title("EchoVerse 🤖 Chatbot")
st.markdown("Welcome to EchoVerse! I’m EchoBot, your AI assistant for creating audiobooks. Ask me anything!")

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# User input box
user_input = st.text_input("Ask EchoBot something...")

# Handle user input
if user_input:
    response = chatbot_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("EchoBot", response))

# Display chat messages
for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.markdown(message)

# Optional footer
st.markdown("---")
st.caption("EchoVerse © 2025 | AI-powered audiobook creation.")
