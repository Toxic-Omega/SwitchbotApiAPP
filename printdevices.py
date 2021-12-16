import requests
import pprint
import os

auth = input('Switchbot Deveploper Token : ')

headers = {
    'Authorization': ''+auth+'',
}

response = requests.get('https://api.switch-bot.com/v1.0/devices', headers=headers)
pprint.pprint(response.json())
os.system("pause")
