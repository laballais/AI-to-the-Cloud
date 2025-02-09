from ollama import Client

client = Client(host='http://localhost:9090')
response = client.chat(model='gemma2:9b', messages=[
    {
        'role': 'user',
        'content': 'What makes the color white look white?',
    },
])

print(response['message']['content'])