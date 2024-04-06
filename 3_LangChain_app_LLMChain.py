from secret_key import open_api_key
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

os.environ["OPENAI_API_KEY"] = open_api_key

app_llm = OpenAI(temperature=0.7)

prompt_template_name = PromptTemplate(
    input_variables=['song_type'],
    template="I want a new {song_type} song. Suggest a fancy name for this song"
)

chain_name = LLMChain(llm=app_llm, prompt=prompt_template_name)
name = chain_name.invoke("Rock")

print(name["text"])
