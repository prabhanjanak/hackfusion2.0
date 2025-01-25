import streamlit as st
import requests

# API key setup
API_KEY = "AIzaSyBjkLf3kyz9T3RqVtkvhmV-BqK8Y8DJEKE"

# Function to interact with the Google Gemini API
def get_response_from_gemini(prompt):
    try:
        # Replace with the actual endpoint URL for the Gemini API
        api_url = "https://gemini.googleapis.com/v1/chat:complete"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        payload = {
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 200
        }
        response = requests.post(api_url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json().get("choices", [])[0].get("message", {}).get("content", "No response received.")
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit UI
st.title("RightBrothers Legal Chatbot")
st.markdown("Ask legal questions, and I'll provide answers based on legal context!")

user_query = st.text_input("Enter your question here:", "")
if st.button("Get Answer"):
    if user_query.strip():
        with st.spinner("Thinking..."):
            response = get_response_from_gemini(user_query)
        st.success("Here's the response:")
        st.write(response)
    else:
        st.warning("Please enter a valid question.")

st.sidebar.title("About RightBrothers")
st.sidebar.markdown("RightBrothers is your trusted legal assistant chatbot.")
