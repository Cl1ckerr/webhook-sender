from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/907427309055787028/fXhgfTYXLPHVWz99QbPGVjU9eNIiNoyMvb3qs04UbU_Sq4Uzu5xWiKEqJlLsHZVy1R24', content='Esta Va Para <@652254918622707778>')

with open("C:/Users/jrodr/Downloads/265f02a95ab74ff49bc21d2b8ded177a.m4a", "rb") as f:
    webhook.add_file(file=f.read(), filename='Esta Va Para Sudo.mp3')

response = webhook.execute()