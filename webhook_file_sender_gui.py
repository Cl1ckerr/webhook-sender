from discord_webhook import DiscordWebhook, DiscordEmbed
import time
import os
import easygui
from tqdm import tqdm
print("Webhook File Sender By Cl1cker")
webhookurl = input("Insert Your Webhook URL: ")
webhookmessage = input("Insert Your Webhook Message: ")
webhookfilename = input("Insert Your File Name With The extension (The name you want the file to have): ")
print("please pick a file to upload")
time.sleep(2)
file = easygui.fileopenbox()
# sexo
webhook = DiscordWebhook(url=f'{webhookurl}', content=f'{webhookmessage}')

with open(f"{file}", "rb") as f:
    webhook.add_file(file=f.read(), filename=f'{webhookfilename}')

response = webhook.execute()
