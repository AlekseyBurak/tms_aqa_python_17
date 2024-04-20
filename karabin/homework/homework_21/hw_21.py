import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.qa-practice.com/elements/input/simple")
# time.sleep(2)
buttons = driver.find_element(By.LINK_TEXT, "Buttons")
buttons.click()
# time.sleep(2)
select_button = driver.find_element(By.LINK_TEXT, "Looks like a button")
select_button.click()
# time.sleep(2)
select_button = driver.find_element(By.LINK_TEXT, "Disabled")
select_button.click()
# time.sleep(2)
selecting_button = driver.find_element(By.NAME, "select_state")
selecting_button.click()
select = Select(selecting_button)
select.select_by_value("enabled")
button = driver.find_element(By.NAME, "submit")
button.click()
# time.sleep(2)
driver.get("https://www.qa-practice.com/elements/input/simple")
inputs = driver.find_element(By.LINK_TEXT, "Inputs")
inputs.click()
select_input = driver.find_element(By.LINK_TEXT, "Text input")
select_input.click()
select_input = driver.find_element(By.LINK_TEXT, "Email field")
select_input.click()
select_input = driver.find_element(By.LINK_TEXT, "Password field")
select_input.click()
input_psw = driver.find_element(By.NAME, "password")
input_psw.send_keys("Qwer!123\n")
