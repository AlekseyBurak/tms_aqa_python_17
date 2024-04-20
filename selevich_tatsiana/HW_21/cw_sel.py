import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/")
# time.sleep(3)
# print(driver.title, driver.current_url)
# element = driver.find_element(By.ID,"maincontent")
# element2 = driver.find_element(By.CLASS_NAME,"page-main")
# element3 = driver.find_element(By.TAG_NAME,"main")
# element4 = driver.find_element(By.LINK_TEXT,"Women")
# element5 = driver.find_element(By.PARTIAL_LINK_TEXT,"men")
# print(element)
# print(element.tag_name)
# print(element.text)


button = driver.find_element(By.CSS_SELECTOR, ".action.more.button")
print(button.text)
button.click()
time.sleep(5)

text_input = driver.find_element(By.ID, "search")
text_input.send_keys("jacket")
text_input.submit()
# text_input.clear()

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

# driver.close()
