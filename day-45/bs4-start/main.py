from bs4 import BeautifulSoup
# import lxml

with open('./day-45/bs4-start/website.html') as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title.string)
# print(soup.p)

all_anchor_tags = soup.find_all(name='a')
# for tag in all_anchor_tags:
#     print(f"{tag.getText()} = {tag.get('href')}")
    
heading = soup.find(name='h1', id='name')
# print(heading)
section_heading = soup.find(name='h3', class_ = 'heading')
# print(section_heading)

company_url = soup.select_one(selector='p a')
# print(company_url.get('href'))

class_name = soup.find(name='h3', class_='heading').get('class')
print(class_name)