import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = 'https://www.melon.com/chart/month/index.htm'
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")


# lst50 = soup.select(".lst50")
# lst100 = soup.select(".lst100")

# lst_all = lst50 + lst100

lst_all = soup.find_all(class_=['lst50', 'lst100'])

for i in lst_all:
    rank = i.select_one('.rank').text
    title = i.select_one('.ellipsis.rank01 > span > a').text
    singer = i.select_one('.ellipsis.rank02 > a').text
    rank_change_number = i.select('.rank_wrap > span')[1].text
    
    
    print(f'순위 : [{rank}]')
    print(f'순위 변동 : {rank_change_number}')
    print(f'노래명 : {title}')
    print(f'가수명 : {singer}')
    print()
