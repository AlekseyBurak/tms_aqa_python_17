import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/catalogsearch/result/?q=jacket")
button = driver.find_element(By.CLASS_NAME, "fc-button-label")
button.click()
# # text_input = driver.find_element(By.ID, "search")
# text_input.send_keys("jacket")
# text_input.submit()
# # yoga_button = driver.find_element(By.CSS_SELECTOR, ".action.more.button")
# # yoga_button.click()
# time.sleep(5)
# text_input = driver.find_element(By.ID, "search")
# text_input.clear()


drop_down = driver.find_element(By.ID, "sorter")
select = Select(drop_down)
select.select_by_index(1)
time.sleep(5)
drop_down = driver.find_element(By.ID, "sorter")
select = Select(drop_down)
select.select_by_value("name")
time.sleep(5)
drop_down = driver.find_element(By.ID, "sorter")
select = Select(drop_down)
select.select_by_visible_text("Relevance")
time.sleep(5)



# element = driver.find_element(By.CLASS_NAME, "page-main")
# element_link = driver.find_element(By.LINK_TEXT, "Women")
# print(element)
# print(element.tag_name)
# print(element.text)
# time.sleep(5)
# print(element_link.text)
