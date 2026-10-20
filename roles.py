import ollama

message= [
    {
        "role": "system",
        "content":"you are a .strict professor.answer in 3 bullet points "
    },
    {
        "role": "user",
        "content":"what is ai"
    }
]

response=ollama.chat(model="llama3.2:latest",messages=message)
print(response.message.content)