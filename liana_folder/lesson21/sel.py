import time

from selenium import webdriver
from selenium.webdriver.common.options import BaseOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/catalogsearch/result/index/?product_list_order=price&q=jacket")


time.sleep(5)
# element_by_id = driver.find_element(By.ID, "maincontent")
#
# element_by_class = driver.find_element(By.CLASS_NAME, "page-main")
#
# element_link = driver.find_element(By.TAG_NAME, "main")
#
# element_part_link = driver.find_element(By.PARTIAL_LINK_TEXT, "men")

# yoga_button = driver.find_element(By.CSS_SELECTOR, ".action.more.button")

# text_input = driver.find_element(By.ID, "search")
# text_input.send_keys("jacket")
# text_input.submit()
# time.sleep(5)
# text_input = driver.find_element(By.ID, "search")
# text_input.clear()

select = Select(driver.find_element(By.ID, "sorter"))

drop_down = driver.find_element(By.ID, "sorter")
select_drop = Select(drop_down)
select.select_by_index(1)
time.sleep(5)

drop_down = driver.find_element(By.ID, "sorter")
select_dropp = Select(drop_down)
select.select_by_value("price")
time.sleep(5)

drop_down = driver.find_element(By.ID, "sorter")
select_droppp = Select(drop_down)
select.select_by_visible_text("Relevance")
time.sleep(5)


