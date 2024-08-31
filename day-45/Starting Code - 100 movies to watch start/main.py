import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

movies = soup.find_all(name='h3', class_ = 'title')
list_movies = [movie.getText() for movie in reversed(movies)]
with open('./day-45/Starting Code - 100 movies to watch start/movie_list.txt', mode='w', encoding='utf-8') as file:
    for movie in list_movies:
        file.write(f'{movie}\n')

