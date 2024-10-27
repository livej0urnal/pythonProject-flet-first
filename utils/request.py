import requests

url = 'https://api.telegram.org/bot'

#function for get updates from api telegram
def getUpdate(token):
    result = requests.get(f'{url}{token}/getUpdates').json()
    return print(result)

# function for send in channel bot message
def sendMessage(token, channel, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': channel,
        'text': text,
        'parse_mode': 'HTML'
    }
    print(f"Sending message to URL: {url} with payload: {payload}")  # Логи для отладки
    response = requests.post(url, data=payload)
    return response.json()


