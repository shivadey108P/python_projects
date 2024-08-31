import requests
from bs4 import BeautifulSoup

class Bill_Board_Songs:
    def __init__(self, date) -> None:
        self.date = date
        self.billboard_url = 'https://www.billboard.com/charts/hot-100'
        
    def get_top_100_songs(self):
        response = requests.get(f"{self.billboard_url}/{self.date}/")
        billboard_response = response.text
        soup = BeautifulSoup(billboard_response, 'html.parser')
        top_100_song_soup = soup.select(selector='li ul li h3')

        top_100_songs_list = ["".join(song.getText().strip()) for song in top_100_song_soup]
        return top_100_songs_list