from secret_key import open_api_key, serp_api_key
import os

os.environ["OPENAI_API_KEY"] = open_api_key
os.environ["SERPAPI_API_KEY"] = serp_api_key


from langchain_openai import OpenAI

app_llm = OpenAI(temperature=0.7)

from langchain.agents import load_tools, initialize_agent, AgentType

tools = load_tools(["serpapi", "llm-math"], llm=app_llm)

agent = initialize_agent(
    tools=tools,
    llm=app_llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

response = agent.invoke("What was the GDP of Europe in 2022? Add 4 to the result")
print(response)