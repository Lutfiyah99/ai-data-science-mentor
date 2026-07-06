import streamlit as st
from chatbot import generate_response
from config import (
    APP_NAME,
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
    WELCOME_MESSAGE,
    INPUT_PLACEHOLDER
)

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT
)

if "messages" not in st.session_state:
    st.session_state.messages = []
    
with st.sidebar:
        
    st.title("⚙️ Pengaturan")
        
    mode = st.selectbox(
        "Mode Belajar",
        [
        "Beginner",
        "Intermediate",
        "Expert"
        ]
    )
    
    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

st.title(APP_NAME)
st.caption(f"📚 Mode Belajar: {mode}")
st.markdown(WELCOME_MESSAGE)
st.divider()

for message in st.session_state.messages:
    
    with st.chat_message(message["role"]):
        st.markdown(message["content"]) 

user_input = st.chat_input(INPUT_PLACEHOLDER)

if user_input:
    st.session_state.messages.append(
    {
        "role": "user",
        "content": user_input
    }
    )

    with st.chat_message("user"):
        st.markdown(user_input)
        
    with st.spinner("AI sedang berpikir..."):
        response = generate_response(
            question=user_input,
            mode=mode,
            chat_history=st.session_state.messages
        )
        
    with st.chat_message("assistant"):
        st.markdown(response)
        
    st.session_state.messages.append(
        {
        "role": "assistant",
        "content": response
        }
        )

