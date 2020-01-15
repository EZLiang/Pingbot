import discord
import sys

client = discord.Client()

@client.event
async def on_message(msg):
    if msg.content == client.user:
        return
    elif client.user in msg.mentions:
        await client.send_message(msg.channel, "_I have been pinged by {}!_".format(msg.author.mention))

def main():
    client.run(sys.argv[1])
