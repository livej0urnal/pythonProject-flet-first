import requests

url = 'https://api.telegram.org/bot'

#function for get updates from api telegram
def getUpdate(token):
    result = requests.get(f'{url}{token}/getUpdates').json()
    return print(result)

# getUpdate('8159762497:AAFpOwtJcTQ3-00APg4AfabhRB9pF77CJKE')

def sendMessage(token, channel, text):
    try:
        return requests.post(
            url=f'{url}{token}/sendMessage',
            data={'chat_id': channel, 'text': text}
        )