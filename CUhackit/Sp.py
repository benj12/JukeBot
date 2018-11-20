import Config
import spotipy

class Sp(object):
    def __init__(self):
        self.sp = spotipy.Spotify(auth=Config.get_spotify_token())
        self.play_list = Config.PLAYLIST_ID

    def search(self, artist="", name=""):
        results = self.sp.search(q="{} {}".format(artist, name), type="track")
        # Needs to be in try/except block
        id = results['tracks']['items'][0]['id']
        track = "spotify:track:"+str(id)
        self.sp.user_playlist_add_tracks(self.sp.me()['id'], self.play_list, [track], position = None)
