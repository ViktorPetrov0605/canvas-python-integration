import os
from openai import OpenAI
from openapi_llm.client.openapi import OpenAPIClient

#CANVAS_API_TOKEN="2464~xTDWAKexVeazXxKJu2mFyhhNNmkca3Lm2GncGm8hM64aB6Ry6W23vTnRGeMVUtEn"
API_KEY="sk-fcab163dc6a9412798cffb078ede266b"
# Create the client from a spec URL (or file path, or raw string)
service_api = OpenAPIClient.from_spec(
    openapi_spec="openapi.json",
    credentials=API_KEY
)

# Initialize your chosen LLM provider (e.g., OpenAI)
client = OpenAI(api_key="sk-fcab163dc6a9412798cffb078ede266b", base_url="https://ai1.viktorpetrov.tech/api")

# Ask the LLM to call the SerperDev API
response = client.chat.completions.create(
    model="qwen3-assistant",
    messages=[{"role": "user", "content": "List all models currently running in ollama"}],
    tools=service_api.tool_definitions,  # LLM tool definitions from the client
)
print(service_api.tool_definitions)
# Now actually invoke the OpenAPI call based on the LLM's generated tool call
service_response = service_api.invoke(response)
print(service_response)
