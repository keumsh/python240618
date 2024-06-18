import re

def is_valid_email(email):
    # 이메일 주소에 대한 정규 표현식
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# 샘플 이메일 주소 목록
emails = [
    "example@example.com",
    "user.name+tag+sorting@example.com",
    "user.name@example.co.uk",
    "user@example",
    "user@.com",
    "user@com",
    "user@site.com",
    "user@site..com",
    "user@site.c",
    "user@-example.com",
    "user@site_com"
]

# 이메일 주소 검사 결과 출력
for email in emails:
    print(f"{email} is {'valid' if is_valid_email(email) else 'invalid'}")
