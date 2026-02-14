import streamlit as st
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from src.search import RAGSearch
import time

# ----------------------
# Load environment variables
# ----------------------
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
client = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.1-8b-instant",
    temperature=0.1,
    max_tokens=1024
)

# ----------------------
# Cache RAG instance
# ----------------------
@st.cache_resource
def load_rag():
    return RAGSearch()

rag_search = load_rag()

# ----------------------
# Page config
# ----------------------
st.set_page_config(page_title="Research Chatbot", page_icon="🤖", layout="wide")

# ----------------------
# Sidebar
# ----------------------
with st.sidebar:
    st.title("📚 Research Bot")
    st.markdown(
        """
        This chatbot answers your queries based on myyyy research papers.
        - Uses **RAG + FAISS** for retrieval
        - Powered by **GROQ LLM**
        """
    )
    if st.button("Clear Conversation"):
        st.session_state.messages = []

# ----------------------
# Session state
# ----------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 Talk to my Reeeeesearch!")

# ----------------------
# CSS for chat styling
# ----------------------
st.markdown(
    """
    <style>
    .chat-container {
        display: flex;
        flex-direction: column;
        max-height: 70vh;
        overflow-y: auto;
        padding-right: 10px;
    }
    .user-message {
        background-color: #d0f0c0;
        color: #000000;
        padding: 10px;
        border-radius: 12px;
        margin-bottom: 8px;
        max-width: 70%;
        align-self: flex-end;
        box-shadow: 1px 1px 4px rgba(0,0,0,0.1);
    }
    .assistant-message {
        background-color: #f0f0f0;
        color: #000000;
        padding: 10px;
        border-radius: 12px;
        margin-bottom: 8px;
        max-width: 70%;
        align-self: flex-start;
        box-shadow: 1px 1px 4px rgba(0,0,0,0.1);
    }
    /* Dark mode */
    @media (prefers-color-scheme: dark) {
        .user-message {
            background-color: #2e7d32;
            color: #ffffff;
        }
        .assistant-message {
            background-color: #4a4a4a;
            color: #ffffff;
        }
    }
    </style>
    """, unsafe_allow_html=True
)

# ----------------------
# Chat container
# ----------------------
for message in st.session_state.messages:
    role_class = "user-message" if message["role"] == "user" else "assistant-message"
    prefix = "👤" if message["role"] == "user" else "🤖"
    
    # Assistant messages in an expander if long
    if message["role"] == "assistant" and len(message["content"]) > 250:
        with st.expander(f"{prefix} Assistant Response"):
            st.markdown(f'<div class="{role_class}">{message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'{prefix} <div class="{role_class}">{message["content"]}</div>', unsafe_allow_html=True)

# ----------------------
# User input
# ----------------------
if prompt := st.chat_input("Type your message here..."):
    
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f'👤 <div class="user-message">{prompt}</div>', unsafe_allow_html=True)
    
    # Typing animation placeholder
    placeholder = st.empty()
    placeholder.markdown("🤖 Assistant is typing...")
    
    # Simulate short delay for typing animation
    time.sleep(0.5)
    
    # Get RAG response
    summary = rag_search.search_and_summarize(prompt, top_k=3)
    
    # Remove typing placeholder
    placeholder.empty()
    
    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": summary})
    
    if len(summary) > 250:
        with st.expander("🤖 Assistant Response"):
            st.markdown(f'<div class="assistant-message">{summary}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'🤖 <div class="assistant-message">{summary}</div>', unsafe_allow_html=True)

# import streamlit as st
# from langchain_groq import ChatGroq
# import os
# from dotenv import load_dotenv
# from src.search import RAGSearch

# # Load environment variables
# load_dotenv()

# # Initialize GROQ client
# groq_api_key = os.getenv("GROQ_API_KEY")
# client = ChatGroq(
#     groq_api_key=groq_api_key,
#     model_name="llama-3.1-8b-instant",
#     temperature=0.1,
#     max_tokens=1024
# )

# # Cache RAG instance to avoid reloading
# @st.cache_resource
# def load_rag():
#     return RAGSearch()

# rag_search = load_rag()

# # Page configuration
# st.set_page_config(page_title="Research Chatbot", page_icon="🤖", layout="wide")

# # Sidebar
# with st.sidebar:
#     st.title("📚 Research Bot")
#     st.markdown(
#         """
#         This chatbot answers your queries based on my research papers.
#         - Uses **RAG + FAISS** for retrieval
#         - Powered by **GROQ LLM**
#         """
#     )
#     if st.button("Clear Conversation"):
#         st.session_state.messages = []

# # Initialize session state
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# st.title("🤖 Talk to my Reeeeesearch!")

# # Custom CSS for chat messages
# st.markdown(
#     """
#     <style>
#     /* Container flex */
#     .chat-container {
#         display: flex;
#         flex-direction: column;
#     }

#     /* User message bubble */
#     .user-message {
#         background-color: #d0f0c0;  /* soft green */
#         color: #000000;              /* black text */
#         padding: 10px;
#         border-radius: 12px;
#         margin-bottom: 8px;
#         max-width: 70%;
#         box-shadow: 1px 1px 4px rgba(0,0,0,0.1);
#     }

#     /* Assistant message bubble */
#     .assistant-message {
#         background-color: #f0f0f0;  /* light gray */
#         color: #000000;
#         padding: 10px;
#         border-radius: 12px;
#         margin-bottom: 8px;
#         max-width: 70%;
#         box-shadow: 1px 1px 4px rgba(0,0,0,0.1);
#     }

#     /* Dark mode overrides */
#     @media (prefers-color-scheme: dark) {
#         .user-message {
#             background-color: #2e7d32;  /* darker green */
#             color: #ffffff;
#         }
#         .assistant-message {
#             background-color: #4a4a4a;  /* medium gray */
#             color: #ffffff;
#         }
#     }
#     </style>
#     """, unsafe_allow_html=True
# )

# # Display chat history
# for message in st.session_state.messages:
#     role_class = "user-message" if message["role"] == "user" else "assistant-message"
#     st.markdown(f'<div class="{role_class}">{message["content"]}</div>', unsafe_allow_html=True)

# # User input
# if prompt := st.chat_input("Type your message here..."):

#     # Add user message
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)

#     # Get response from RAG
#     summary = rag_search.search_and_summarize(prompt, top_k=3)

#     # Add assistant message
#     st.session_state.messages.append({"role": "assistant", "content": summary})
#     st.markdown(f'<div class="assistant-message">{summary}</div>', unsafe_allow_html=True)
