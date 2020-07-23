from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")
driver.get("https://map.kakao.com/")

time.sleep(2)

# '강남 마라탕' 검색
input_box = driver.find_element_by_css_selector("input#search\.keyword\.query")
input_box.send_keys("강남 마라탕")
input_box.send_keys(Keys.ENTER)

time.sleep(1)

# 15개의 가게 컨테이너 한꺼번에 추출
stores = driver.find_elements_by_css_selector("li.PlaceItem")

# 가게 하나씩 정보 추출
for store in stores:
    name = store.find_element_by_css_selector("a.link_name").text
    try:
        phone = store.find_element_by_css_selector("span.phone").text
    except:
        phone = "번호 없음"
    try:
        addr = store.find_element_by_css_selector("p").text
    except:
        addr = "주소 없음"

    print(name, phone, addr)

# 팝업 창(?) 미리 제거
driver.find_element_by_css_selector("div.view_coach").click()

# '장소 더 보기' 버튼 클릭
more_place_btn = driver.find_element_by_css_selector("a#info\.search\.place\.more")
more_place_btn.send_keys("\n")

time.sleep(1)

# 2페이지부터 10페이지까지 크롤링하도록 범위 설정
for n in range(2, 11):

    # 매 페이지가 로딩될 때 time.sleep
    time.sleep(1)

    # 현재 페이지에 있는 가게 컨테이너들 한꺼번에 추출
    stores = driver.find_elements_by_css_selector("li.PlaceItem")

    # 가게 컨테이너들 하나씩 가게 이름, 가게 전화번호, 가게 주소 추출
    for store in stores:
        name = store.find_element_by_css_selector("a.link_name").text
        try:
            phone = store.find_element_by_css_selector("span.phone").text
        except:
            phone = "번호 없음"
        try:
            addr = store.find_element_by_css_selector("p").text
        except:
            addr = "주소 없음"

        print(name, phone, addr)

    # '이전' 버튼, 1, 2, 3, 4, 5, '다음' 버튼을 모두 포함한 것들 한꺼번에 추출
    page_bar = driver.find_elements_by_css_selector(
        "div#info\.search\.page div.pageWrap > *"
    )

    # 5로 나눈 나머지가 0이 아닐 때만 1, 2, 3, 4, 5에 해당하는 index에 맞게 페이지 이동
    if n % 5 != 0:
        page_bar[n % 5 + 1].click()

    # 5로 나눈 나머지가 0일 때는 현재 페이지가 5, 10, ... 페이지라는 뜻이므로 '다음' 버튼 클릭
    else:
        page_bar[6].click()

# 마지막까지 크롤링이 제대로 됐는지 브라우저에서 확인하기 위한 용도
time.sleep(10)

driver.close()
