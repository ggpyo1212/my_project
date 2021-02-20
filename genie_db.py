import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 아래 빈 칸('')을 채워보세요
data = requests.get('https://www.genie.co.kr/chart/top200', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')


# 아래 빈 칸('')을 채워보세요
for tr in trs:
    rank = tr.select_one('td.number').text[0:2].strip()
    title = tr.select_one('td.info > a.title.ellipsis').text.strip()
    artist = tr.select_one('td.info > a.artist.ellipsis').text
    imgUrl = tr.select_one('td > a > img')['src']
    onclick2 = tr.select_one('td > a')['onclick']
    onclick1 = onclick2.replace("fnViewAlbumLayer('","")
    onclick = onclick1.replace("');return false;","")
    url = 'https://www.genie.co.kr/detail/albumInfo?axnm='


    genei = {
        'rank': rank,
        'title': title,
        'artist': artist,
        'imgUrl': imgUrl,
        'url': url + onclick1.replace("');return false;",""),
    }

    db.genie.insert_one(genei)
    print(genei)
