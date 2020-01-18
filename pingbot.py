import discord, sys, asyncio


client = discord.Client()


active = True


def parse(string):
    ends = {"s": 1, "m": 60, "h": 3600, "d": 86400, "y": 31536000}
    return ends[string[-1]] * int(string[0:-1])


def handle(args, ch):
    global active
    if args[0] == "on":
        active = True
        return True
    elif args[0] == "off":
        active = False
        return False
    elif args[0] == "ping":
        u = "@" + args[1]
        delay = "0s"
        if len(args) > 2:
            delay = args[2]

        async def warn():
            if "#" in args[1]:
                await ch.send("Pinging {} in {}".format(args[1].split("#")[0], delay))
            elif args[1][-1] in "aeiou":
                await ch.send("Pinging {}s far and wide in {}".format(args[1], delay))
            else:
                await ch.send("Pinging {}es far and wide in {}".format(args[1], delay))
        asyncio.run(warn())

        async def ping():
            await asyncio.sleep(parse(delay))
            await ch.send(u)
        asyncio.run(ping())
        return False
    elif args[0] == "spam":
        u = "@" + args[1]

        async def ping():
            await ch.send(u)
        for i in range(int(args[2])):
            asyncio.run(ping())
        return False


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    elif client.user in msg.mentions:
        if handle(msg.content[len(client.user.mention)].split(" "), msg.channel) and active:
            await msg.channel.send("_I have been pinged by {}!_".format(msg.author.mention))


def main():
    client.run(sys.argv[1])


if __name__ == "__main__":
    main()
