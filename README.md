# know-my-research

Overview

This project is a Retrieval-Augmented Generation (RAG) chatbot built with Python, Streamlit, FAISS, and LangChain/GROQ LLM. It allows users to interactively query research papers or any textual dataset, generating responses based on retrieved relevant content rather than only pre-trained knowledge.

The chatbot features a modern UI with animated gradient backgrounds, black chat bubbles, avatars, expanders for long responses, and a clear conversation button.

Features

RAG-powered QA: Answers are generated using a FAISS vector store combined with a GROQ LLM for factual and grounded responses.

FAISS vector store: Efficient similarity search over your research documents.

Streamlit UI:

Scrollable chat container

Black chat bubbles with avatars (👤 user, 🤖 assistant)

Expanders for long responses

Typing animation placeholder

Clear conversation button at the top

Animated gradient background: Blue → purple → black gradient for a modern look.

Dark/light mode compatible: Chat bubbles and interface maintain readability in both modes.

Try it out at know-my-research.streamlit.app
