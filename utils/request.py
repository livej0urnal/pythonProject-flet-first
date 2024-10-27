import requests

url = 'https://api.telegram.org/bot/'

#function for get updates from api telegram
def getUpdate(token):
    result = requests.get(f'{url}{token}/getUpdates').json()
    return print(result)

# function for send in channel bot message
def sendMessage(token, channel, text):
    try:
        return requests.post(
            url=f'{url}{token}/sendMessage',
            data={'chat_id': channel, 'text': text, 'parse_mode': 'HTML'}
        ).json()
    except Exception as error:
        return print(error)


