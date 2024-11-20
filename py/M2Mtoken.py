import time
import requests
import json

# Initialize the token data
token_data = {
    'access_token': None,
    'received_at': 0.0,
    'expires_in': 0.0
}


def get_access_token(client_id, client_secret):
    url = "https://auth.haiper.ai/oauth/token"
    headers = {'content-type': 'application/json'}
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "audience": "https://api1.haiper.ai/v1",
        "grant_type": "client_credentials"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()


def update_token_data(client_id, client_secret):
    global token_data
    response = get_access_token(client_id, client_secret)
    token_data['access_token'] = response['access_token']
    token_data['received_at'] = time.time()
    token_data['expires_in'] = response['expires_in']


def get_token(client_id, client_secret):
    global token_data
    # If the token is None or going to expire, update the token
    if token_data['access_token'] is None or (time.time() - token_data['received_at'] + 600) >= token_data['expires_in']:
        update_token_data(client_id, client_secret)
    return token_data['access_token']

