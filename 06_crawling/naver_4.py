import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

#접속하고자 하는 주소입력 => url
base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
search_url = input("검색어를 입력해주세요 : ")

url = base_url + search_url
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

title = soup.select(".title_link._cross_trigger")
name = soup.select(".user_info > a") # > : 바로 다음에 오는 태그를 선택할 때 사용할 수 있음.

for i in zip(title, name):
    print(f"제목 : {i[0].text}") # (title, name)
    print(f"출처 : {i[1].text}")
    print(f"링크 : {i[0]['href']}")
    print()
    