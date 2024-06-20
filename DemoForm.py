#DemoForm.py
#DemoFrom.ui(화면) + DemoForm.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#디자인 파일 로딩
from_class = uic.loadUiType("DemoForm.ui")[0]
#폼클래스 정의
class DemoForm(QDialog, from_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면")

#진입점 체크
if __name__ == "__main__":
    app=QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec()