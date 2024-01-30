from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time


# 옵션 설정33
options = Options()
user = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
options.add_argument(f'User-Agent={user}')
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=options)

# 크롤링 코드 작성
url = 'https://kream.co.kr/'
driver.get(url)

driver.find_element(By.CSS_SELECTOR, '.btn_search').click()
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, '.input_search.show_placeholder_on_focus').send_keys('슈프림')
time.sleep(0.3)

driver.find_element(By.CSS_SELECTOR, '.input_search.show_placeholder_on_focus').send_keys(Keys.ENTER)
time.sleep(0.2)

for i in range(40):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.SPACE)
    time.sleep(0.2)
    # 부분 캡쳐하는 법
    # driver.save_screenshot(f'/Users/mac/Desktop/oz_class/06_crawling/kream_screenshot/supreme{i}.png')
    
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

items = soup.select('.item_inner')

num = 1
for i in items:
    brand_name = i.select_one('.product_info_brand.brand')
    product_name = i.select_one('.translated_name')
    price = i.select_one('.amount')
    
    if '후드' in product_name.text:
        print(f'No.{num}')
        print(f'브랜드명 : {brand_name.text}')
        print(f'상품명 : {product_name.text}')
        print(f'가격 : {price.text}')
        print()
        num += 1

driver.quit()