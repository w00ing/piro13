import time
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")

driver.get("https://papago.naver.com")


driver.implicitly_wait(3)
input_box = driver.find_element_by_id("txtSource")
input_box.send_keys("안녕하세요!")

auto_translate = driver.find_element_by_css_selector(
    "#root > div > div.wrap___1rX6i.many_lang.rwd.rwd___3Qe-c.global___1SQCJ.banner_active___3MQbf > section > div > div.rwd_layout___2qH8c > div:nth-child(2) > div > div.autocomplete_area___2alwE.active___3VPGL > label"
)

auto_translate.click()

translate_btn = driver.find_element_by_css_selector("#btnTranslate")
translate_btn.click()

output_box = driver.find_element_by_css_selector("#txtTarget > span")
print(output_box.text)
