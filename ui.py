import chainlit as cl
from google.oauth2 import service_account
import google.auth.transport.requests
import requests, json
from rich import print

key_path = "key.json"
cloud_url = ""

@cl.on_message
async def main(message: cl.Message):
    # Authenticate and get the ID token
    credentials = service_account.IDTokenCredentials.from_service_account_file(
        key_path,
        target_audience=cloud_url
    )
    credentials.refresh(google.auth.transport.requests.Request())
    id_token_value = credentials.token

    headers = {
        'Authorization': f'Bearer {id_token_value}',
        'Content-Type': 'application/json'
    }

    response = requests.post(
        cloud_url + '/api/generate',
        headers=headers,
        json={
            "model": "gemma2:9b",
            "prompt": message.content,
            "stream": False
        },
        stream=False
    )

    # Parse and send the response back to the Chainlit UI
    result = json.loads(response.text)["response"]
    await cl.Message(content=result).send()