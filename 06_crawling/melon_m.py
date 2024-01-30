from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#옵션 설정
options = Options()
user = "Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/121.0.0.0"
options.add_argument('user-agent=' + user)

options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

#크롤링 코드 작성
url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(2)

if driver.current_url != url:
    driver.get(url)
    time.sleep(2)
    
driver.find_element(By.LINK_TEXT, '닫기').click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, '멜론차트').click()
time.sleep(2)

more_btn = driver.find_elements(By.CSS_SELECTOR, '#moreBtn')[1].click()
time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

chart_list = soup.select('#_chartList')

for i in chart_list:
    rank = i.select_one('.ranking_num').text.strip()
    title = i.select_one('.title.ellipsis').text.strip()
    singer = i.select_one('.name.ellipsis').text.strip()
    
    # 노래 차트순위
    print(f'현재 순위 : {rank}')
    # 노래 제목
    print(f'노래 제목 : {title}')
    # 가수 이름
    print(f'가수 이름 : {singer}')
    print()
    

