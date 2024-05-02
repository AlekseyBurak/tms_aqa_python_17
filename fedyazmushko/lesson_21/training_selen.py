import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com")
#
# element_by_id = driver.find_element(By.ID, "maincontent")
#
# element_by_class = driver.find_element(By.CLASS_NAME, "main")
#
# element_by_tag = driver.find_element(By.TAG_NAME, "main")
#
# element_link = driver.find_element(By.LINK_TEXT, "Women")

# yoga_button = driver.find_element(By.CSS_SELECTOR, ".action.more.button")
# yoga_button.click()

text_input = driver.find_element(By.ID, "search")
text_input.send_keys("jacket")
text_input.submit()
time.sleep(5)
text_input.clear()

time.sleep(5)