from bs4 import BeautifulSoup
import requests

url = 'http://mignews.com/mobile'

page = requests.get(url)

print(page.status_code)

soup = BeautifulSoup(page.text, "html.parser")

allNews = []
allNews = soup.findAll("div", {"class": "text-color-dark"})
# filteredNews = []
# for data in allNews:
#     if data.find('span', class_='time2 time3') is not None:
#         filteredNews.append(data.text)
for data in allNews:
    print(data)