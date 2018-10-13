# Work withPython 3.6
import discord

TOKEN = 'NTAwNjY3NzU2NzUzMDU5ODQ5.DqOLTA.w6CuBzCPmBHJI2KrOEhyOHaK_5E'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
	
        await client.send_message(message.channel, msg)
app.get('/login', function(req, res)) {
var scopes = 'user-read-private user-read-email';
res.redirect('https://accounts.spotify.com/authorize' +
  '?response_type=code' +
  '&client_id=' + ef8f0c90eaa6411191ee56607f82d6de +
  (scopes ? '&scope=' + encodeURIComponent(scopes) : '') +
  '&redirect_uri=' + encodeURIComponent(redirect_uri));
});
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
