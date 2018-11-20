import discord
import Config



class JukeBot(discord.Client):
    def __init__(self, *args, **kwards):
        discord.Client.__init__(self)
        self.commands = {
            '!Yeet' : self.yeet,
            '!AddSong' : self.add_song,
        }

    async def on_ready(self):
        print("Logged on as {0}".format(self.user))

    async def on_message(self, message):
        if message.author != client.user:
            for command in self.commands:
                if message.content.startswith(command):
                    await self.commands[command](message.channel, message.content[len(command):])

    async def yeet(self, channel, message):
        await super().send_message(channel, "Yeet")

    async def add_song(self, message):
        pass

if __name__ == "__main__":
    client = JukeBot()
    client.run(Config.DISCORD_TOKEN)
