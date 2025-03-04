import streamlit as st
import os
from datetime import date
from langchain_core.messages import AIMessage,HumanMessage
from src.langgraphagenticai.ui.uiconfigfile import config

class LoadStreamlitUI:
    def __init__(self):
        self.config = config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config()

