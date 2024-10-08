import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

SPOTIFY_ID = os.environ['SPOTIFY_CLIENT_ID']
SPOTIFY_SECRET_KEY = os.environ['SPOTIFY_CLIENT_SECRET']
BASE_URL = 'https://api.spotify.com.'
USERNAME_SPOTIFY = os.environ['USERNAME']
SPOTIFY_REDIRECT_URI = os.environ['REDIRECT_URI']


class Spotify_Setup:
    def __init__(self) -> None:
        pass
    def get_current_user(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=SPOTIFY_ID,
                client_secret=SPOTIFY_SECRET_KEY,
                redirect_uri=SPOTIFY_REDIRECT_URI,
                scope='playlist-modify-private',
                show_dialog=True,
                cache_path='./day-46/token.txt',
                username=USERNAME_SPOTIFY))  
        self.user_id = self.sp.current_user()['id'] 
        
        return self.user_id
    
    def get_song_results(self,year,song_list):
        self.year = year
        self.song_list = song_list
        self.song_uris = []
        for song in song_list:
            result = self.sp.search(q=f"track:{song} year: {year}", type='track')
            try:
                uri = result["tracks"]["items"][0]["uri"]
                self.song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")
        return self.song_uris
    
    def create_playlist(self, date):
        self.date = date
        self.playlist = self.sp.user_playlist_create(user=self.user_id, name=f"{self.date} Billboard 100", public= False)
        pprint(self.playlist)
        
        self.sp.playlist_add_items(playlist_id=self.playlist['id'], items= self.song_uris)