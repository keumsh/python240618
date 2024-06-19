import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

search_keyword='맥북에어'

url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}'

response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

# create a new Excel workbook and select the active sheet\
wb = Workbook()
ws = wb.active

# write the column names to the first row of the sheet
ws.append(["블로그명", "블로그주소", "글 제목", "포스팅 날짜"])

for page in range(1, 100):
    url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page * 10 - 9}'

    posts = soup.find_all('div', {'class':'fds-ugc-block-mod-list mX3YIi0JzyVIEmRuhQNH'})
    for post in posts:
        try:
            #<a nocr="1" href="https://blog.naver.com/dltmdgns2525/223481920092" class="YHttveyJzmt1VC2oZeAc fds-comps-right-image-text-title" target="_blank" data-cb-target="'SYS-0000000038366979.90000003_0000000000000034088F7A5C'" data-cb-trigger="true"><span class="YWfQTkWtVZ5k77j0gKAe"><mark>맥북 에어</mark> M3 15인치 M2 비교 총정리</span></a>
            #<span class="YWfQTkWtVZ5k77j0gKAe"><mark>맥북 에어</mark> M3 15인치 M2 비교 총정리</span>
            blog_address_elem = post.find("a", 
                attrs={"class":"YHttveyJzmt1VC2oZeAc fds-comps-right-image-text-title"}) 
            blog_address = blog_address_elem["href"]
            blog_address_title_elem = post.find("span", attrs={"class":"YWfQTkWtVZ5k77j0gKAe"})
            blog_address_title = blog_address_title_elem.text 
        except TypeError:
            blog_address = "" 
            blog_address_title = ""
        
        # <span class="fds-info-sub-inner-text YWfQTkWtVZ5k77j0gKAe">2일 전</span>
        post_date_elem = post.find('span', {'class':'fds-info-sub-inner-text YWfQTkWtVZ5k77j0gKAe'})
        post_date = post_date_elem.text if post_date_elem else ""
        post_title_elem = post.find("a", attrs={"class":"YHttveyJzmt1VC2oZeAc fds-comps-right-image-text-title"})
        post_title = post_title_elem.text if post_title_elem else "" 

        print(blog_address)
        print(blog_address_title)
        print(post_title)
        print(post_date)

        ws.append([blog_address_title, blog_address, post_title, post_date])

#path = 'c:\\work\\'
#file_path = f'{path}{search_keyword}_blog_data.xlsx'
file_path = f'{search_keyword}_blog_data.xlsx'
wb.save(file_path)