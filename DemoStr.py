# DemoStr.py

strA = "파이썬은 강력해"
strB = "python is very powerful"

print(len(strA))
print(len(strB))
print(strB.capitalize())
print(strB.upper())

data = "<<<  spam and ham  >>>"
result = data.strip("<> ")# 작다, 크다, 빈칸은 제거해
print(data)
print(result)
result2 = result.replace("spam", "spam egg")
print(result2)
lst = result2.split()
print(lst)
print(":)".join(lst))

#정규표현식
import re

result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

#선택한 블럭 주석처리 : ctrl + /
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

result = re.search("\d{4}", "올해는 2024년")
print(result.group())

result = re.search("\d{5}", "우리 동네는 52333")
print(result.group())

result = re.search("apple", "this is apple")
print(result.group())