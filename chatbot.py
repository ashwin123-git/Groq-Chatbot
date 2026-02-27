import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    print("Error: GROQ_API_KEY not found in .env file")
    exit(1)

client = Groq(api_key=API_KEY)

messages = []

while True:
    user_input = input("\nYou: ").strip()
    if not user_input:
        continue
    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append({"role": "user", "content": user_input})

    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    reply = chat_completion.choices[0].message.content
    print(f"Bot: {reply}")
    messages.append({"role": "assistant", "content": reply})
