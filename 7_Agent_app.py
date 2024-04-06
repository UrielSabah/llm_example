from secret_key import open_api_key
import os

os.environ["OPENAI_API_KEY"] = open_api_key


from langchain_openai import OpenAI

app_llm = OpenAI(temperature=0.7)

from langchain.agents import load_tools, initialize_agent, AgentType

tools = load_tools(["wikipedia", "llm-math"], llm=app_llm)

agent = initialize_agent(
    tools=tools,
    llm=app_llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

response = agent.invoke("When was Golda Meir born and what was her age on the kipur war?")
print(response)