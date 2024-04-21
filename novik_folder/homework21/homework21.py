import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.qa-practice.com/")
element_by_text = driver.find_element(By.LINK_TEXT, "Text input")
element_by_text.click()
element_by_name = driver.find_element(By.NAME, "text_string")
element_by_name.send_keys("hello")
print(element_by_name.get_attribute('value'))


element_by_link_text = driver.find_element(By.LINK_TEXT, "Buttons")
element_by_link_text.click()
element_by_id = driver.find_element(By.ID, "submit-id-submit")
element_by_id.click()
found_result = driver.find_element(By.CLASS_NAME, "result-text")
print(found_result.text)

element_by_link_text2 = driver.find_element(By.LINK_TEXT, "Disabled")
element_by_link_text2.click()
element_dropdown_by_name = driver.find_element(By.NAME, "select_state")
select = Select(element_dropdown_by_name)
select.select_by_visible_text("Disabled")
select.select_by_value("enabled")
button_find = driver.find_element(By.NAME, "submit")
button_find.click()
found_result = driver.find_element(By.CLASS_NAME, "result-text")
print(found_result.text)