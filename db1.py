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

# db1.py 
import sqlite3

#연결객체 리턴(메모리에서 작업) 
con = sqlite3.connect(":memory:")

#구문을 실행할 커서 객체 리턴
cur = con.cursor() 

#테이블 생성
cur.execute("create table PhoneBook (Name text, PhoneNum text);")

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
# for row in cur:
#     print(row[0], row[1]) 

#레코드 포인터가 가리키는 것을 가지고 옴
print("----fetchone()-------")
print(cur.fetchone())
print("---fetchmany(2))---")
print(cur.fetchmany(2))
print("---fetchall()---")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())

