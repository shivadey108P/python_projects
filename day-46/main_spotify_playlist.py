from billboard import Bill_Board_Songs
from spotify_settings import Spotify_Setup
from pprint import pprint
date = input('Which year would you like to travel to? Type the date in this format (YYYY-MM-DD): ')
billboard_songs = Bill_Board_Songs(date)
year = date.split('-')[0]
spotify_songs = Spotify_Setup()

songs_list =  billboard_songs.get_top_100_songs()
user_id = spotify_songs.get_current_user()
result_of_song_search = spotify_songs.get_song_results(year=year, song_list=songs_list)
pprint(result_of_song_search)
create_playlist = spotify_songs.create_playlist(date=date)


