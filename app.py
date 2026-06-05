import streamlit as st

st.title("🚀 My AI & Data Intelligence Hub")
st.write("Welcome to my professional portfolio dashboard.")

# Quick test input for your future Google AI Studio integration
user_input = st.text_input("Ask a question to the AI model:")
if user_input:
    st.write(st.write(f"Testing pipeline connection. You typed: {user_input}"))
