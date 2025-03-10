import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json


class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase= usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase= self.usecase
        graph = self.graph
        user_message = self.user_message
        if usecase =="Basic Chatbot":
                for event in graph.stream({"messages":("user",user_message)}):
                    print(event.values())
                    for value in event.values():
                        print(value['messages'])
                        with st.chat_message("user"):
                            st.write(user_message)
                        with st.chat_message("assistant"):
                            st.write(value["messages"][-1].content)
        
        elif usecase == "Chatbot with Tool":
             initial_state = {"messages":[user_message]}
             res = graph.invoke(initial_state)
             for message in res["messages"]:
                    if type(message) == HumanMessage:
                        with st.chat_message('user'):
                                st.write(message.content)
                    elif type(message) == ToolMessage:
                        with st.chat_message("Tool"):
                                st.write("Tool call started")
                                st.write(message.content)
                                st.write("Tool call ended")
                    elif type(message) == AIMessage and message.content:
                        with st.chat_message("Assistant"):
                                st.write(message.content)
                       