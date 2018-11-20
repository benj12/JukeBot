# Jukebot

## Config Object
- - -
In order to use JukeBot, you need a Config.py file in a format similar to this:
```import spotipy.util as util

DISCORD_TOKEN = "token"
PLAYLIST_ID = "token"
SP_USERNAME = "username"

def get_spotify_token():
    return util.prompt_for_user_token(
        'spotify username',
        scope="user-read-private playlist-modify-private",
        client_id="spotify client id",
        client_secret="client secret",
        redirect_uri="some uri"
    )
```
