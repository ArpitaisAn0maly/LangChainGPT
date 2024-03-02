from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory




memory = ConversationBufferMemory(memory_key="chat-history", return_messages=True,output_key='answer')

tools = load_tools (['wikipedia'], llm=model)

agent = initialize_agent(
            tools,
            agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
            verbose=True,
            llm=model)

response = {}
response['input'] = "Can you please provide a quick summary of Napoleon Bonaparte? \
                          Then do a separate search and tell me what the commonalities are with Serena Williams"
response['chat_history'] = []
res = agent.run(response) 