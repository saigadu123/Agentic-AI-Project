from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.tools.search_tool import get_tavily_search_tool

class ChatbotWithToolNode:
    """ 
    Chatbot logic enhanced with tool integration
    """
    def __init__(self,model):
        self.llm = model

    def process(self,state:State):
        """ 
        Processes the input state and generates response with the tool integration.
        """
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role":"user","content":user_input}])
        
        # Tool invocation
        tool = get_tavily_search_tool()
        tools_response = tool.invoke({"query":user_input})
        return {"messages": [llm_response,tools_response]}
    
    def create_chatbot(self,tools):
        """ 
        Returns a chatbot node function.
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state:State):
            """ 
            Chatbot logic for processing the input state and returning the response.
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}
        
        return chatbot_node
