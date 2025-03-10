from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """ 
    Return the list of tools to be used in the chatbot
    """
    tools = [get_tavily_search_tool()]
    return tools


def create_tool_node(tools):
    """ 
    Creates and returns the tool nodes
    """
    return ToolNode(tools=tools)

def get_tavily_search_tool():
    """ 
    Returns the tavily search tool
    """
    tavily_search_tool = TavilySearchResults(max_results=2)
    return tavily_search_tool