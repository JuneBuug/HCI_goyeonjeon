import requests
from bs4 import BeautifulSoup
from hci.models import Score

# HTTP GET Request
req = requests.get('https://namu.wiki/w/%EA%B3%A0%EC%97%B0%EC%A0%84/%EC%97%AD%EB%8C%80%20%EC%A0%84%EC%A0%81')

html = req.text


soup = BeautifulSoup(html, 'html.parser')

for tag in soup.find_all('tr'):

    list = []
    #'19' in td_tag.text or '20' in td_tag.text and
    for td_tag in tag.find_all('td'):
        list.append(td_tag.text)

        # 무[2] 이런 식으로 나오는 데이터를 없애주기 위해서
        for item in list:
            if '[' in item:
                index = item.find('[')
                list[list.index(item)] = item[:index]

    if len(list) > 2 and len(list[0]) == 4 and ' 경기취소 ' not in list : # 취소경기가 없었던 해
        Score.objects.create(year=list[0], baseball_k=list[1],baseball_y=list[2],baseball_r=list[3],baseketball_k=list[4],baseketball_y=list[5],baseketball_r=list[6],ice_k=list[7],ice_y=list[8],ice_r=list[9],football_k=list[10],football_y=list[11],football_r=list[12],soccer_k=list[13],soccer_y=list[14],soccer_r=list[15],total_k=list[16],total_tie=list[17],total_y=list[18],total_r=list[19])
