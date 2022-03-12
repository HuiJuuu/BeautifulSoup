import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/index'
response = requests.get(url)

if response.status_code == 200:
    #print("Success")
    source = response.text
    soup = BeautifulSoup(source, 'html.parser')
    print("soup", soup)

    #ex = soup.find_all("ol", {"class": "asideBoxRank asideBoxRank2"})

    #print("ex", ex)








# from urllib import request
# imgUrl = soup.find("img")["src"]
# #urlretrieve는 다운로드 함수
# urllib.request.urlretrieve(imgUrl, 'test.jpg')
# col1, col2 = st.beta_columns(2)
