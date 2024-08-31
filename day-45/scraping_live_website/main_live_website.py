from bs4 import BeautifulSoup
import requests
from pprint import pprint
import pandas as pd

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')
span_tags = soup.find_all(name='span', class_='titleline')
top_30_links = []
top_30_news = []
top_30_score_points = []
for tag in span_tags:
    anchor_tag = tag.find('a')
    if anchor_tag:
        href = anchor_tag.get('href')
        text = anchor_tag.getText()
        # print(f"{text}: {href}")
        top_30_links.append(href)
        top_30_news.append(text)
        
score_points = soup.find_all(name='span', class_= 'score')
for score in score_points:
    top_30_score_points.append(int(score.getText().split()[0]))
top_news = {
    
    'News': top_30_news,
    'Link': top_30_links,
    'Score': top_30_score_points
    }

# df = pd.DataFrame(top_news)

# df_sorted = df.sort_values(by='Score', ascending=False).reset_index(drop=True)

# print(df_sorted)
max(top_news['Score'])