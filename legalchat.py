import streamlit as st
import google.generativeai as genai

# Configure the API key directly
api_key = "AIzaSyBjkLf3kyz9T3RqVtkvhmV-BqK8Y8DJEKE"

# Set up the API key for Google Gemini
genai.configure(api_key=api_key)

# Load the Gemini Pro model and start the chat
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Function to get responses from the Gemini API
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize the Streamlit app
st.set_page_config(page_title="RightBrothers Legal Chatbot")
st.title("RightBrothers Legal Chatbot")
st.markdown("Ask legal questions, and I'll provide answers based on legal context!")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input field and submit button
user_query = st.text_input("Enter your question here:")
submit = st.button("Ask the question")

if submit and user_query.strip():
    # Get response from Gemini API
    with st.spinner("Fetching response..."):
        response = get_gemini_response(user_query)
    
    # Add user query and response to the chat history
    st.session_state['chat_history'].append(("You", user_query))
    st.subheader("Response:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Display the chat history
st.subheader("Chat History")
for role, text in st.session_state['chat_history']:
    st.write(f"**{role}:** {text}")
