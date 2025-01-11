import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

developer_message = "You are a helpful assistant."
messages = [{"role": "developer", "content": developer_message}]

def send_message(message):
    messages.append({"role": "user", "content": message})

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    response = completion.choices[0].message.content

    messages.append({"role": "assistant", "content": response})
    print(response)

def main():
    while True:
        message = input()
        send_message(message)

if __name__ == "__main__":
    main()