import discord
import Config
import Sp

class JukeBot(discord.Client):
    def __init__(self):
        discord.Client.__init__(self)
        # Dictionary of commands available
        self.commands = {
            '!Yeet' : self.yeet,
            '!AddSong' : self.add_song,
            '!SongData': self.song_data,
            '!Commands': self.help,
            '!Help': self.help,
            '!help': self.help,
        }
        self.channel = None
        self.help_str = None
        self.sp = Sp.Sp()
    async def on_ready(self):
        print("Logged on as {0}".format(self.user))

    async def on_message(self, message):
        if message.author != client.user:
            for command in self.commands:
                if message.content.startswith(command):
                    await self.commands[command](message.channel, message.content[len(command):])

    async def yeet(self, channel, message):
        await super().send_message(channel, "Like my father always used to say . . . YEET!")

    async def add_song(self, channel, message):
        if not ';' in message:
            await super().send_message(channel, "Invalid format! Try adding ; between song and artist!")
        else:
            song, artist = message.split(';')
            try:
                self.sp.search(artist,song)
                await super().send_message(channel, "Artist:{}\nSong:{}".format(artist,song))
            except:
                await super().send_message(channel, "Song Not Found!")
    
    async def help(self, channel, message):
        if self.help_str is None:
            self.help_str = "Available Commands:\n`"
            for key in self.commands.keys():
                if key == "!AddSong":
                    self.help_str += "{} {}\n".format(key, "[song name];[artist]")
                else: 
                    self.help_str += "{}\n".format(key)
        await super().send_message(channel, self.help_str+'`')

    async def song_data(self, channel, message):
        pass

if __name__ == "__main__":
    client = JukeBot()
    client.run(Config.DISCORD_TOKEN)
