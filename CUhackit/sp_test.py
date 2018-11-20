import Config
import spotipy

token = Config.get_j_token()
sp = spotipy.Spotify(auth=token)

results = sp.search(q="{} {}".format("","1999"),type="track")
id = results['tracks']['items'][0]['id']
track = 'spotify:track:'+str(id)
sp.user_playlist_add_tracks(sp.me()['id'],Config.PLAYLIST_ID, [track], position=None)
