import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/index'
response = requests.get(url)

if response.status_code == 200:
    print("Success")
    source = response.text
    soup = BeautifulSoup(source, 'html.parser')
    print("soup", soup)

    print("soup", soup.h1)

    for ch in soup.h1.children :
        print(ch)