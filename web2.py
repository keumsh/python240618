#web2.py
#웹서버와 통신
import requests
#크롤링
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    titleElem = post.find("h2", attrs={"class":"card-title"})
    priceElem = post.find("div", attrs={"class":"card-price"})
    addrElem = post.find("div", attrs={"class":"card-region-name"})
    title = titleElem.text.strip()
    price = priceElem.text.strip()
    addr = addrElem.text.strip()
    #파이썬 3/6 f-string 문법 , 변수형을 바로 넘길수 있다.
    print(f"{title},{price},{addr}")

#  <div class="card-desc">
#       <h2 class="card-title">아이폰 14 프로</h2>
#       <div class="card-price ">
#         270,000원
#       </div>
#       <div class="card-region-name">
#         경기도 고양시 일산서구 탄현동
#       </div>