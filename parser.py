import requests
from bs4 import BeautifulSoup
from hci.models import CheerioDance


# HTTP GET Request
req = requests.get('https://www.youtube.com/results?search_query=%EA%B3%A0%EB%A0%A4%EB%8C%80%ED%95%99%EA%B5%90+%EC%9D%91%EC%9B%90%EB%8B%A8')

html = req.text


soup = BeautifulSoup(html, 'html.parser')

for tag in soup.find_all('h3', {'class': 'yt-lockup-title'}):

    for a_tag in tag.find_all('a'):
        href, title = a_tag.get('href'), a_tag.get('title')
        if 'watch' in href:
            # print([href,title])
            CheerioDance.objects.create(title=title, video_url='https://www.youtube.com'+href)

# 그냥 manage.py에서 실행함