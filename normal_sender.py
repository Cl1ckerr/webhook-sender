import requests, os
from discord_webhook import DiscordWebhook, DiscordEmbed
from colorama import Fore, Style, init

webhookurl = input("Insert Your Webhook URL: ")
webhooktitle = input("Insert Your Wewbhook Title: ")
webhooktitledesc = input("Insert Your Wewbhook Title Description: ")
webhookauthor = input("Insert Your Wewbhook Author: ")
webhookauthorurl = input("Insert Your Wewbhook Author Image URL: ")
webhookimageurl = input("Insert Your Wewbhook Image URL: ")
webhookthumbnailurl = input("Insert Your Wewbhook Thumbnail URL: ")
webhookfooter = input("Insert Your Wewbhook Footer: ")
webhookfield1 = input("Insert Your Wewbhook Field 1: ")
webhookfield1desc = input("Insert Your Wewbhook Field 1 Description: ")
webhookfield2 = input("Insert Your Wewbhook Field 2: ")
webhookfield2desc = input("Insert Your Wewbhook Field 2 Description: ")
webhookfield3 = input("Insert Your Wewbhook Field 3: ")
webhookfield3desc = input("Insert Your Wewbhook Field 3 Description: ")
# sexo

webhook = DiscordWebhook(url=f'{webhookurl}')

# create embed object for webhook
embed = DiscordEmbed(title=f'{webhooktitle}', description=f'{webhooktitledesc}', color='03b2f8')

# set author
embed.set_author(name=f'{webhookauthor}', url=f'{webhookauthorurl}')

# set image
embed.set_image(url=f'{webhookimageurl}')

# set thumbnail
embed.set_thumbnail(url=f'{webhookthumbnailurl}')

# set footer
embed.set_footer(text=f'{webhookfooter}')

# set timestamp (default is now)
embed.set_timestamp()

# add fields to embed
embed.add_embed_field(name=f'{webhookfield1}', value=f'{webhookfield1desc}')
embed.add_embed_field(name=f'{webhookfield2}', value=f'{webhookfield2desc}')
embed.add_embed_field(name=f'{webhookfield3}', value=f'{webhookfield3desc}')

# add embed object to webhook
webhook.add_embed(embed)

response = webhook.execute()
