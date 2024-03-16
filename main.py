from pprint import pprint

import requests

bot_token = '7180878079:AAESanYVJBhBeuxfoJRvqBoOfThhJVdlcb4'
channel_id = '-4196259554'


def show_updates(token):
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(url)
    pprint(response.json())


def send_message(message, token=bot_token, chat_id=channel_id):
    print(message)
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, json=payload)
    return response.json()


def main():
    message = 'Hello! This is a test message.'
    response = send_message(message)
    print(response)


if __name__ == "__main__":
    main()
