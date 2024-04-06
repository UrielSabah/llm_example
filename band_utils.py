from secret_key import open_api_key
import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

os.environ["OPENAI_API_KEY"] = open_api_key
app_llm = OpenAI(temperature=0.7)


def generate_bandname_and_songlist(song_type):
    prompt_template_name = PromptTemplate(
        input_variables=['song_type'],
        template="I want a new {song_type} song. Suggest a fancy name for this song",
    )

    prompt_template_items = PromptTemplate(
        input_variables=['song_name'],
        template="Suggest some band names for {song_name}. Return it as a comma separated list",
    )

    chain_name = LLMChain(llm=app_llm, prompt=prompt_template_name, output_key="song_name")
    chain_items = LLMChain(llm=app_llm, prompt=prompt_template_items, output_key="band_name_list")

    chain = SequentialChain(
        chains=[chain_name, chain_items],
        input_variables=["song_type"],
        output_variables=["song_name", "band_name_list"]
    )

    response = chain.invoke({"song_type": "Rap"})

    return response
