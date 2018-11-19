import spotipy
import sys
import spotipy.util as util
import discord
import requests

import Config
TOKEN = Config.DISCORD_TOKEN
token = Config.get_spotify_token()
playlist_id = Config.PLAYLIST_ID
client = discord.Client()
with open("cache.dat", "w") as f:
	f.write(" ")

@client.event
async def on_message(message):
	spotify = spotipy.Spotify(auth = token)
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return
	print(message.author)
	if str(message.author) == 'JukeBot#0000':
		print("We're here!")
		if message.content == "!SongData":
			with open("cache.dat", "r") as f:
				info = "Data :"
				for line in f:
					info += line
				await client.send_message(message.channel, info)

	elif len(message.content) > 0:
		input = message.content.split(";")
		try:
			name = input[0]
			artist = input[1]
			print("The Artist is: " + str(artist))
			print("The Song is: " + str(name))
			await client.send_message(message.channel, "The Artist is: "+ str(artist) + ",  The Song is: "  + str(name))


#artist = 'Big Time Rush'
#name = 'Til I Forget About You'

			results = spotify.search(q=artist + ' ' + name, type='track')

			user = spotify.me()['id']
			id = results['tracks']['items'][0]['id']
			track = 'spotify:track:' + str(id)
			with open("cache.dat", "a") as f:
				f.write("name:{0}, track:{1}\n".format(name, artist))
			playlist_id = "0H8I9G80Nv1y7K59LgrATv"
			spotify.user_playlist_add_tracks(user, playlist_id, [track], position = None)
		except:
			await client.send_message(message.channel, "You sent garbage")

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

if __name__=="__main__":
	client.run(TOKEN)
