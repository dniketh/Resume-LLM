import streamlit as st
from ingest import ingest_resumes
from retriever import ResumeRetriever
import os

st.set_page_config(page_title="Resume Ranking Assistant", layout="wide")

def initialize_chat_history():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "retriever" not in st.session_state:
        st.session_state.retriever = ResumeRetriever()
    else:
        if isinstance(st.session_state.retriever, ResumeRetriever):
            st.session_state.retriever.reset_state()

def main():
    st.title("AI-Powered Resume Assistant")
    
    # File upload and processing
    with st.sidebar:
        st.header("Configuration")
        if st.button("Process Resumes"):
            with st.spinner("Analyzing resumes..."):
                ingest_resumes()
                st.success("Resumes processed successfully!")
        if st.button('Reset Chat'):
            st.session_state.retriever.reset_state()
            st.session_state.messages = []
    
    initialize_chat_history()
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask about the resumes..."):
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.retriever.chat(prompt)
                st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main() 