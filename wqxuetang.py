from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time

# url = input('阅读网址：')
url = 'https://lib-nuanxin.wqxuetang.com/read/pdf/3208245'
browser = webdriver.Chrome()

browser.get(url)
time.sleep(2)
page_number_input_box = browser.find_element_by_class_name('page-head-tol')
page_number_msg = page_number_input_box.text


page_number_msg = re.findall('\d+', page_number_msg)
page_current = int(page_number_msg[0])
page_number_total = int(page_number_msg[1])
print(page_current, page_number_total)


page_box = browser.find_element_by_id('pagebox')
print(page_box)

for i in range(100, page_number_total+1):
    # browser.find_element_by_id('input').click()
    try:
        page_number_input_box.click()
    except:
        pass
    time.sleep(0.1)
    browser.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div/div[1]/div[2]').send_keys(i)
    # page_number_input_box.send_keys(i)
    page_number_input_box.send_keys(Keys.ENTER)
    time.sleep(1)





time.sleep(100)
browser.close()

