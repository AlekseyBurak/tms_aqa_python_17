import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.options import BaseOptions
from selenium.webdriver.support.ui import Select

driver = webdriver.Edge()
driver.maximize_window()
# driver.get("https://magento.softwaretestingboard.com")
# element = driver.find_element(By.ID, "maincontent")
# print(element)
# print(element.tag_name)
# print(element.text)

# driver.get("https://magento.softwaretestingboard.com")
# element = driver.find_element(By.CLASS_NAME, "page-main")
# print(element)
# print(element.tag_name)
# print(element.text)

# driver.get("https://magento.softwaretestingboard.com")
# element = driver.find_element(By.TAG_NAME, "main")
# print(element)
# print(element.tag_name)
# print(element.text)

# driver.get("https://magento.softwaretestingboard.com")
# element = driver.find_element(By.LINK_TEXT, "Women")
# print(element)
# print(element.tag_name)
# print(element.text)

# driver.get("https://magento.softwaretestingboard.com")
# yoga_button = driver.find_element(By.CSS_SELECTOR, ".action.more.button")
# yoga_button.click()
# time.sleep(5)

# driver.get("https://magento.softwaretestingboard.com")
# yoga_button = driver.find_element(By.CSS_SELECTOR, ".action.more.button")
# yoga_button.click()
# time.sleep(5)

# driver.get("https://magento.softwaretestingboard.com")
# text_input = driver.find_element(By.ID, "search")
# text_input.send_keys("jacket")
# text_input.submit()
# time.sleep(5)
# text_input = driver.find_element(By.ID, "search")
# text_input.clear()
# time.sleep(5)

driver.get("https://magento.softwaretestingboard.com/catalogsearch/result/index/?product_list_order=price&q=jacket")
drop_down = driver.find_element(By.ID, "sorter")
select = Select(drop_down)
select.select_by_index(0)
time.sleep(5)
drop_down = driver.find_element(By.ID, "sorter")
select = Select(drop_down)
select.select_by_value("price")
time.sleep(5)
drop_down = driver.find_element(By.ID, "sorter")
select = Select(drop_down)
select.select_by_visible_text("Relevance")
time.sleep(5)
