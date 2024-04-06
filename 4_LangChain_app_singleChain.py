# song generator
from secret_key import open_api_key
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
import os

os.environ["OPENAI_API_KEY"] = open_api_key
app_llm = OpenAI(temperature=0.7)

prompt_template_name = PromptTemplate(
    input_variables=['song_type'],
    template="I want a new {song_type} song. Suggest a fancy name for this song"
)

prompt_template_items = PromptTemplate(
    input_variables=['band_name'],
    template="Suggest some band names for {band_name}. Return it as a comma separated list"
)

chain_name = LLMChain(llm=app_llm, prompt=prompt_template_name)
chain_items = LLMChain(llm=app_llm, prompt=prompt_template_items)

chain = SimpleSequentialChain(chains=[chain_name, chain_items])

response = chain.invoke("Rap")

print(response["output"])
