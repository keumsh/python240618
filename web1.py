#web1.py
#웹크롤링을 위한 선언
from bs4 import BeautifulSoup

#웹페이지를 로딩:메서드 체인
page = open("Chap09_test.html", "rt", encoding= "utf-8").read()
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#검색
#print(soup.prettify())
#<P>를 몽땅 검색
#print(soup.find_all("p"))
#첫번째<p>를 검색
#print(soup.find("p"))
#조건검색: <p class="outer-tesxt">
#print(soup.find_all("p", class_="outer-text"))
#속성들을 검색 : attrs 요즘 사용
#print(soup.find_all("p", attrs={"class":"outer-text"}))
#id 속성으로 검색
#print(soup.find_all(id="first"))

#태그 내부 문자열 추출 : .text, .get_text()
for tag in soup.find_all("p"):
    title = tag.text
    title = title.replace("\n","")
    print(title)

