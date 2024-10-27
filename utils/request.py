import requests

url = 'https://api.telegram.org/bot'

def getUpdate(token):
    result = requests.get(f'{url}{token}/getUpdates').json()
    return print(result)