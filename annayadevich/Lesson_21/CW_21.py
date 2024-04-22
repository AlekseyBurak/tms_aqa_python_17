import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
# driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/catalogsearch/result/index/?product_list_order=price&q=jacket")

drop_down = driver.find_element(By.ID, "sorter")
select = Select(drop_down)
select.select_by_index(1)
time.sleep(5)
drop_down = driver.find_element(By.ID, "sorter")
select = Select(drop_down)
select.select_by_value("price")
time.sleep(5)
drop_down = driver.find_element(By.ID, "sorter")
select = Select(drop_down)
select.select_by_visible_text("Relevance")
time.sleep(5)



# yoga_button = driver.find_element(By.CSS_SELECTOR, ".action.more.button")
# yoga_button.click()

# text_input = driver.find_element(By.ID, "search")
# text_input.send_keys("jacket")
# text_input.submit()
# time.sleep(5)
# text_input = driver.find_element(By.ID, "search")
# text_input.clear()
#
# time.sleep(5)


# yoga_button = driver.find_element(By.LINK_TEXT, "Shop New Yoga")
# print(yoga_button.text)
# yoga_button.click()
# time.sleep(10)




#element_by_class = driver.find_element(By.CLASS_NAME, "page-main")

# time.sleep(5)
# driver.close()
# time.sleep(5)
# driver.quit()
# time.sleep(5)