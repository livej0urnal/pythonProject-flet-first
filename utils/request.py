import requests

url = 'https://api.telegram.org/bot'

#function for get updates from api telegram
def getUpdate(token):
    result = requests.get(f'{url}{token}/getUpdates').json()
    return print(result)