#DemoForm2.py
#DemoFrom2.ui(화면) + DemoForm.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

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
        self.label.setText("첫번째 버튼 클릭")
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