import ollama

response=ollama.generate(model="llama3.2:latest",prompt="explain how ai works in one line")
print(response.response)

