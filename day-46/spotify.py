import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

SPOTIFY_ID = os.environ['SPOTIFY_CLIENT_ID']
SPOTIFY_SECRET_KEY = os.environ['SPOTIFY_CLIENT_SECRET']
BASE_URL = 'https://api.spotify.com.'

class Spotify_Setup:
    def __init__(self) -> None:
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=SPOTIFY_ID,
                client_secret=SPOTIFY_SECRET_KEY,
                redirect_uri='https://open.spotifywithshivadey.com/',
                scope='playlist-modify-private',
                show_dialog=True))                               