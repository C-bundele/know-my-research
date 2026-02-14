import streamlit as st
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from src.search import RAGSearch


# Load environment variables
load_dotenv()

# Initialize GROQ client
groq_api_key = os.getenv("GROQ_API_KEY")
client = ChatGroq(groq_api_key=groq_api_key,model_name="llama-3.1-8b-instant",temperature=0.1,max_tokens=1024)

@st.cache_resource
def load_rag():
    return RAGSearch()

st.set_page_config(page_title="My Chatbot", page_icon="🤖")

st.title("🤖 Talk to my Reeeeesearch! ")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your message here..."):

    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from OpenAI
    rag_search = load_rag()
    summary = rag_search.search_and_summarize(prompt, top_k=3)
    # response=client.invoke([prompt.format(query=prompt)])
    # reply = response.content

    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": summary})

    with st.chat_message("assistant"):
        st.markdown(summary)
