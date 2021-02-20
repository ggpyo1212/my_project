import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 아래 빈 칸('')을 채워보세요
data = requests.get('https://music.bugs.co.kr/chart/track/realtime/total', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#CHARTrealtime > table > tbody > tr')


# 아래 빈 칸('')을 채워보세요
for tr in trs:
    rank = tr.select_one('td > div > strong').text
    title = tr.select_one('th > p > a').text.strip()
    artist = tr.select_one('td > p > a').text
    imgUrl = tr.select_one('td > a > img')['src']
    url = tr.select_one('td > a')['href']

    bugs = {
        'rank': rank,
        'title': title,
        'artist': artist,
        'imgUrl': imgUrl,
        'url': url,
    }

    # db.genie.insert_one(bugs)
    print(bugs)
