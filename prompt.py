import ollama

#1 role
system_role_content = "you are a wildlife travel writer for a south india travel blog"


#2 task
user_role_content_v1 = "write an introduction to karnataka's wildlife for first time visitors"


#3 constraints
user_role_content_v2 = """"
write an introduction to karnataka's wildlife for first time visitors,
150 words, Audience: city dwellers who have never been on a safari, vivid tone, exactly three parks, no jargon.
"""


#4 format
user_role_content_v3 = """
write an introduction to karnataka's wildlife for first time visitors,
150 words, Audience: city dwellers who have never been on a safari, vivid tone, exactly three parks, no jargon.
format: three bullets (park,signature animal, best month), then a one line closing tip.
"""


#5 Examples
user_role_content_v4 = """
write an introduction to karnataka's wildlife for first time visitors,
150 words, Audience: city dwellers who have never been on a safari, vivid tone, exactly three parks, no jargon.
format: three bullets (park,signature animal, best month), then a one line closing tip.
example bullet: bandipur: wild elephants graze at dusk along the forest edge.best in nov-feb.
"""


messages = [
    {
        "role": "system",
        "content": system_role_content
    },
    {
        "role": "user",
        "content": user_role_content_v4
    }
]
response=ollama.chat(model="llama3.2:latest",messages=messages)
print(response.message.content)