import spotipy
import sys
import spotipy.util as util
import discord
import requests

import Config


TOKEN = Config.DISCORD_TOKEN
playlist_id = Config.PLAYLIST_ID
token = Config.get_spotify_token()

client = discord.Client()

with open("cache.dat", "w") as f:
    f.write(" ")

# appends song data to our cache
def SongData():
    with open("cache.dat", "r") as f:
        info = "Data :"
        for line in f:
            info += line
    return info

# searches for artist. Returns if search was successful
def search_artists(name, artist):
    try:
        results = spotify.search(q=artist+ ' '+name, type='track')
        user = spotify.me()['id']
        id = results['tracks']['items'][0]['id']
        track = 'spotify:track:' + str(id)
        with open("cache.dat", "a") as f:
            f.write("name:{0}, track:{1}\n".format(name, artist))
            spotify.user_playlist_add_tracks(user, playlist_id, [track],position = None)
        return True
    except:
        return False

@client.event
async def on_message(message):
    #spotify = spotipy.Spotify(auth = token)
    # we do not want the bot to reply to itself

    if message.author == client.user:
            return
    print(message.author)
    if str(message.author) == 'JukeBot#0000':
        if message.content == "!SongData":
            await client.send_message(message.channel, SongData())

    elif len(message.content) > 0:
        input = message.content.split(";")
        name, artist = input
        await client.send_message(message.channel, "Artist: "+ str(artist) + "\nSong: "  + str(name))
        if search_artists(name, artist):
            await client.send_message(message.channel, "Song added")
        else:
            await client.send_message(message.channel, "Error")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

if __name__=="__main__":
    client.run(TOKEN)
