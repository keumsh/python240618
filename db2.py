#db1.py
import sqlite3

#연결객체 리턴(메모리에서 작업) 
con = sqlite3.connect("sample.db")

#구문을 실행할 커서 객체 리턴
cur = con.cursor() 

#테이블 생성
cur.execute("create table if not exists PhoneBook (Name text, PhoneNum text);")

#1건 입력 
cur.execute("insert into PhoneBook values ('derick','010-222');")
#입력 파라메터 처리 
name = "홍길동"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))

#여러번 실행
datalist = (("전우치","010-567"),("이순신","010-345"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#조회를 실행
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row[0], row[1]) 

#작업을 정상적으로 완료함
con.commit()
