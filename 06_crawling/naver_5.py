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

areas = soup.select(".view_wrap")


for i in areas:
    ad = i.select_one(".link_ad")
    if ad :
        print("광고 구좌 입니다") # continue 사용하면 출력 안되고 생략 가능
    else:
        title = i.select_one(".title_link")
        name = i.select_one(".user_info > a")
        print(title.text)
        print(name.text)
        print(title['href'])
        print()