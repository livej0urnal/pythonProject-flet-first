import requests

url = 'https://api.telegram.org/bot'

#function for get updates from api telegram
def getUpdate(token):
    result = requests.get(f'{url}{token}/getUpdates').json()
    return print(result)

# function for send in channel bot message
def sendMessage(token, channel, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    try:
        response = requests.post(url, data={'chat_id': channel, 'text': text, 'parse_mode': 'HTML'})
        return response.json()
    except Exception as error:
        print("An error occurred:", error)


