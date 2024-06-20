#DemoForm2.py
#DemoFrom2.ui(화면) + DemoForm.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
#웹서버와 통신
import requests
#크롤링
from bs4 import BeautifulSoup



#디자인 파일 로딩
from_class = uic.loadUiType("DemoForm2.ui")[0]

#폼클래스 정의(QMainWindow 상속)
class DemoForm(QMainWindow, from_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯메서드
    def firstClick(self):
        url = "https://www.daangn.com/fleamarket/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        #파일로 저장 (append, read, write)
        f = open("daangn.txt","a+", encoding="utf-8")
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
            f.write(f"{title},{price},{addr}\n")
        f.close()
        self.label.setText("당근마켓 크롤링 완료")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭함")      
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭했음")

#진입점 체크
if __name__ == "__main__":
    app=QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec()