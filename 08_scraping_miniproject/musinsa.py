from bs4 import BeautifulSoup
from selenium import webdriver

#셀레니움에 다양한 옵션을 적용시키기 위한 패키지
from selenium.webdriver.chrome.options import Options

#크롬 드라이버 매니저를 실행시키기 위해 설치해주는 패키지
from selenium.webdriver.chrome.service import Service
#자동으로 크롬 드라이브를 최신으로 유지해주는 패키지 
from webdriver_manager.chrome import ChromeDriverManager
#클래스, 아이디, css_selector를 이용하고자 할때
from selenium.webdriver.common.by import By
#키보드 입력
from selenium.webdriver.common.keys import Keys

import time

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

options_ = Options()
options_.add_argument(f"User-Agent={user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])


#크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options_)

url = "https://www.musinsa.com/"
driver.get(url)
time.sleep(1)

#코트 카테고리 진입
coat_category = driver.find_element(By.CSS_SELECTOR, '.sc-8hpehb-9.eatmFI:nth-child(13)') # :nth-child() 클래스 동일할때 사용
coat_category.click() 
time.sleep(2)

#화면 하단 스크롤
for i in range(10):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.SPACE)
    time.sleep(0.5)


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

product_list = soup.find_all('li', {"class",'li_box'})


# for i in range(len(product_list)):
#     if i == 0:
#         print(product_list[i])
#     else:
#         continue

num = 0
for i in product_list:
    product_brand = i.select_one('.item_title').text.strip()
    product_name = i.select_one('.list_info').text.strip()
    product_price_element = i.select_one('.price')
    if product_price_element: # 챗pgt 활용.. 어우
        product_price = product_price_element.contents[-1].strip()
    else:
        product_price = None


    product_review = i.find('span', {'class':'count'})
    if product_review is None:
        product_review = 0
    else:
        product_review = product_review.text.strip()

    num += 1
    #print("*** 무신사 추천순 랭킹 (겨울 싱글코트 부분) ***")
    print(f'순위 : [{num}]위')
    print(f'브랜드명 : {product_brand}')
    print(f'상품명 : {product_name}')
    print(f'금액 : {product_price}')
    print(f'리뷰 :{product_review}개')
    print()
    


    #2페이지 넘기기

#driver.find_element(By.CSS_SELECTOR, '.paging-btn.btn:contains("2")').click()