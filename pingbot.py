import discord

client = discord.Client()

@client.event
async def on_message(msg):
    if msg.content == client.user:
        return
    elif "@Pingbot#9337" in msg.content:
        await client.send_message(msg.channel, "_I have been pinged by {}!_".format(msg.author.mention))
