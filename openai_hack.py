from openai import OpenAI

client = OpenAI(
    base_url = 'https://ai1.viktorpetrov.tech/ollama',
    api_key='eyJIsInQyNmF', # required, but unused
)

tools = [{
    "type": "function",
    "name": "list_courses",
    "description": "View the currently signed courses.",
    "parameters": {
        "type": "object",
        "properties": {
            }
        },
        "required": [
            ],
        "additionalProperties": False
    }

]

stream = client.responses.create(
    model="gemma3:4b",
    input=[{"role": "user", "content": "Can you be kind enough to check up on my courses at uni?"}],
    tools=tools,
    stream=True
)

for event in stream:
    print(event)    
