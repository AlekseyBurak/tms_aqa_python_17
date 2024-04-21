import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.qa-practice.com/elements/input/simple")

input_button = driver.find_element(By.LINK_TEXT, "Inputs")
input_button.click()

text_input_button = driver.find_element(By.LINK_TEXT, "Text input")
text_input_button.click()
text_input_field = driver.find_element(By.ID, "id_text_string")
text_input_field.send_keys("Some_text")
text_input_field.submit()

email_field = driver.find_element(By.LINK_TEXT, "Email field")
email_field.click()
email_field_input = driver.find_element(By.ID, "id_email")
email_field_input.send_keys("some_email@mail.com")
email_field_input.submit()

password_field = driver.find_element(By.LINK_TEXT, "Password field")
password_field.click()
password_field_input = driver.find_element(By.ID, "id_password")
password_field_input.send_keys("Some_password")
password_field_input.submit()

button_button = driver.find_element(By.LINK_TEXT, "Buttons")
button_button.click()
simple_button = driver.find_element(By.LINK_TEXT, "Simple button")
simple_button.click()
submitted_find = driver.find_element(By.ID, "submit-id-submit")
submitted_find.click()

disabled_button = driver.find_element(By.LINK_TEXT, "Disabled")
disabled_button.click()
disabled_button_list = driver.find_element(By.ID, "id_select_state")
disabled_button_list.click()
disabled_button_list_select = Select(disabled_button_list)
disabled_button_list_select.select_by_value("enabled")
disabled_button_list_select.submit = driver.find_element(By.ID, "submit-id-submit")
disabled_button_list_select.submit.click()


