import openai
from secret_key import open_api_key

openai.api_key = open_api_key

app_messages = []
app_messages.append({"role": "system", "content": "you are a python developer"})

while True:
    user_message = input("User: ")
    app_messages.append({"role": "user", "content": user_message})

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=app_messages
    )

    reply = response.choices[0].message.content
    print("ChatGPT: " + reply)
    app_messages.append({"role": "assistant", "content": reply})
