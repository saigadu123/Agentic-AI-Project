from langgraph.graph import StateGraph,START,END,MessagesState
from langgraph.prebuilt import tools_condition,ToolNode
from langchain_core.prompts import ChatPromptTemplate
import datetime
from src.langgraphagenticai.state.state import State

class GraphBuilder:

    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        

