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

# send photo method
def sendMessagePhoto(token, channel, photo, caption):
    try:
        data = {'chat_id': channel, 'caption': caption}
        link = f'{url}{token}/sendPhoto?chat_id={channel}'
        with open(photo, 'rb') as image_file:
            result = requests.post(link, data=data, files={'photo': image_file})
            result.raise_for_status()  # Проверка на ошибки HTTP
        return result.json()
    except FileNotFoundError:
        print(f"Error: File '{photo}' not found.")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")