from secret_key import open_api_key
import os
from langchain_openai import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

os.environ["OPENAI_API_KEY"] = open_api_key

app_llm = OpenAI(temperature=0.7)

app_memo = ConversationBufferWindowMemory(k=1) #limits the history of the conversation
convo = ConversationChain(llm=app_llm, memory=app_memo)
print(convo.invoke("Who is the president of uruguay?"))
print(convo.invoke("Whats the current today date?"))
print(convo.invoke("Who is the best uruguay soccer player of that year?"))