import ollama

messages=[{"role":"system","content":"you are a friendly assistant."}]

while True:
    user_prompt = input("you:")
    user_role = {"role": "user", "content": user_prompt}

    messages.append(user_role)

    response = ollama.chat(model="llama3.2:latest", messages=messages)
    response = response["message"]["content"]

    print("Assistant:", response)
    assistant_role = {"role": "assistant", "content": response}

    messages.append(assistant_role)