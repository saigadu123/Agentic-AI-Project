from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """ 
    Basic chatbot logic implementation.
    """
    def __init__(self,model):
        self.llm = model
        

    def process(self,state):
        """ 
        Processes the input state and generate the chatbot response
        """
        return {"messages":[self.llm.invoke(state["messages"])]}


    