import discord

client = discord.Client()

@client.event
async def on_message(message):
    if str(message.channel) == "general" and message.content != "":
        await message.channel.purge(limit=1)




client.run("OTM0MjQ0OTIzNTgxMDA1ODg0.YetRYw.9R1QVkYOLCTMi_4FEq75tm5uhfY")

