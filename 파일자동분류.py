#파일 자동 분류
import os
import shutil
import glob

# 다운로드 폴더 경로
download_folder = r'C:\Users\user\Downloads'

# 이동할 폴더들
folders = {
    'images': ['*.jpg', '*.jpeg'],
    'data': ['*.csv', '*.xlsx'],
    'docs': ['*.txt', '*.doc', '*.pdf'],
    'archive': ['*.zip']
}

# 폴더가 없으면 생성
for folder in folders:
    path = os.path.join(download_folder, folder)
    if not os.path.exists(path):
        os.makedirs(path)

# 파일 이동 함수
def move_files(patterns, destination):
    for pattern in patterns:
        for file in glob.glob(os.path.join(download_folder, pattern)):
            shutil.move(file, destination)

# 각 폴더에 맞는 패턴의 파일 이동
for folder, patterns in folders.items():
    destination = os.path.join(download_folder, folder)
    move_files(patterns, destination)

print("파일 이동이 완료되었습니다.")
