import time

from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.options import BaseOptions

from selenium.webdriver.support.ui import Select



# select = Select(driver.find_element(By.NAME, 'name'))
# select.select_by_index(index)
# select.select_by_visible_text("text")
# select.select_by_value(value)

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/catalogsearch/result/index/?product_list_order=price&q=jacket")

# element_by_id = driver.find_element(By.ID, "maincontent")
# element_by_class = driver.find_element(By.CLASS_NAME, "page-main")
# element_by_tag = driver.find_element(By.TAG_NAME, "main")
# element_link = driver.find_element(By.LINK_TEXT, "Women")
# element_part_link = driver.find_element(By.PARTIAL_LINK_TEXT, "men")
# yoga_button = driver.find_element(By.CSS_SELECTOR, ".action.more.button")
# text_input = driver.find_element(By.ID, "search")
#
#
# text_input.send_keys("jacket")
# text_input.submit()
# time.sleep(5)
# text_input = driver.find_element(By.ID, "search")
# text_input.clear()

drop_down = driver.find_element(By.XPATH, '')
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

