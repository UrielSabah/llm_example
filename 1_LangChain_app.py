from secret_key import open_api_key
from langchain_openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = open_api_key

app_llm = OpenAI(temperature=0.7)

name = app_llm.invoke("I want a new rock song. Suggest a fancy name for this")
print(name)
