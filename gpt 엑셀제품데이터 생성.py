import random
import openpyxl
import os

# 데이터 생성
product_ids = [f'P{str(i).zfill(3)}' for i in range(1, 101)]
product_names = [f'Product_{i}' for i in range(1, 101)]
quantities = [random.randint(1, 100) for _ in range(100)]
prices = [round(random.uniform(10.0, 1000.0), 2) for _ in range(100)]

# 엑셀 워크북 생성
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Products"

# 헤더 추가
headers = ['Product ID', 'Product Name', 'Quantity', 'Price']
ws.append(headers)

# 데이터 추가
for i in range(100):
    ws.append([product_ids[i], product_names[i], quantities[i], prices[i]])

# 디렉토리 확인 및 생성
output_dir = r"c:\work2"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 엑셀 파일 저장
output_file = os.path.join(output_dir, "products.xlsx")
wb.save(output_file)

print(f"엑셀 파일이 '{output_file}'로 저장되었습니다.")
