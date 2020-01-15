import discord
import sys

client = discord.Client()

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    elif client.user in msg.mentions:
        await msg.channel.send("_I have been pinged by {}!_".format(msg.author.mention))

def main():
    client.run(sys.argv[1])

if __name__ == "__main__":
    main()
