from google.oauth2 import service_account
import google.auth.transport.requests
import requests, json
from rich import print

key_path = "key.json"
cloud_url = ""
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
        "prompt": "What makes the color white look white?",
        "stream": True      # set stream to False if you are testing response in your console
    },
    # stream = False        # uncomment to set stream to False
)

# Uncommment the code below to print the response to console
# print(response.text)
# print(json.loads(response.text)["response"])

# Stream the response
for line in response.iter_lines():
    if line:
        decoded_line = line.decode('utf-8')
        print(json.loads(decoded_line)["response"], end="", flush=True)