import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "01518462e7b0438b85762e72422ac610"
CLIENT_SECRET = "9be6b8885e8b45d1bdac6c3288dab5eb"

def create_spotify_client():
    client_credentials_manager = SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp
