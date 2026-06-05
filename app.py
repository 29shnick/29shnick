import streamlit as st
from google import genai

st.title("🚀 My AI & Data Intelligence Hub")
st.write("Welcome to my professional portfolio dashboard.")

# This automatically securely connects to the key you saved in Azure!
try:
    client = genai.Client()
    
    user_input = st.text_input("Ask a question to the AI model:")
    if user_input:
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=user_input,
        )
        st.write("### AI Response:")
        st.write(response.text)

except Exception as e:
    st.error("Make sure your API key is properly configured in Azure App Settings.")
