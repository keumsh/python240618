#db1.py
import sqlite3

#연결객체 리턴
con = sqlite3.connect(":memory:")

#구문을 실행할 커서 객체 리턴
cur = con.cursor()

#테이블 생성
cur.execute("create table PhoneBook (Name text, PhoneNum text);")

#1건 입력
cur.execute("insert into PhoneBook values('derick','010-222');")