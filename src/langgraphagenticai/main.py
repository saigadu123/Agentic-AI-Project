import streamlit as st
import json
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error:Failed to load user input from UI")

    #Text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your message:")

    # Initializing the LLM
    if user_message:
        
        obj_llm_config = GroqLLM(user_controls_input=user_input)
        model = obj_llm_config.get_llm_model()

        if not model:
            st.error("Error: LLM model could not be initialized.")
            return 
        
        usecase = user_input.get("selected_usecase")
        if not usecase:
            st.error("Error: Usecase not selected.")
            return
        

        # Graph Builder
        graph_builder = GraphBuilder(model)
        try:
            graph = graph_builder.setup_graph(usecase=usecase)
        except Exception as e:
            raise ValueError(f"Error: Graph set up Failed - {e}")
            return 
        
        # Display Result
        display_obj = DisplayResultStreamlit(
            usecase=usecase,
            graph=graph,
            user_message=user_message
        )
        display_obj.display_result_on_ui()
    
        
 



