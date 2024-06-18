#DemoRandom.py

import random

print(random.random())
print(random.random())

#임의의 정수
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])

print("---유니크한 값 샘플릴----")
print(random.sample(range(20),10))
print(random.sample(range(20),10))

#로또 번호
print(random.sample(range(1,46),5))

#라이브러리 선언
from os.path import *
from os import *
import glob

print(abspath("python.exe"))
print(basename("c:\\work2\\demo.py"))

name = "c:\\python310\\python.exe"
if exists(name):
    print("파일크기:",getsize(name))
else:
    print("파일 없음")