import selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.qa-practice.com/elements/input/simple")

time.sleep(3)

# TASK 1.1 Input field
# Tab "Text input"

text_field = driver.find_element(By.ID, "id_text_string")
text_field.send_keys("Lorem ipsum dolor sit amet")
time.sleep(3)

# TASK 1.2 Input field:
# Tab "Email field"

# Go to Email field
tab_email_field = driver.find_element(By.LINK_TEXT, "Email field")
tab_email_field.click()
time.sleep(3)

# Enter text in email field
email_field = driver.find_element(By.ID, "id_email")
email_field.send_keys("test@mailto.plus")
time.sleep(3)

# TASK 1.3 Input field:
# Tab "Password field"

# Go to Password field
tab_password_field = driver.find_element(By.LINK_TEXT, "Password field")
tab_password_field.click()
time.sleep(3)

# Enter password in password field
password_field = driver.find_element(By.ID, "id_password")
password_field.send_keys("password")
time.sleep(3)

# TASK 2 Buttons:
# Tab "Simple button"

# Go to Simple button page
button_page = driver.find_element(By.LINK_TEXT, "Buttons")
button_page.click()
time.sleep(3)


# Simple button click
button_simple = driver.find_element(By.ID, "submit-id-submit")
button_simple.click()
time.sleep(3)
submitted_text = driver.find_element(By.ID, "result-text")
print("Found text of simple button")
time.sleep(3)

# Go to Looks like a button page
button_page = driver.find_element(By.LINK_TEXT, "Looks like a button")
button_page.click()
time.sleep(3)

# Looks like a button click
looks_like_button = driver.find_element(By.CLASS_NAME, "a-button")
looks_like_button.click()
time.sleep(3)
submitted_text_2 = driver.find_element(By.ID, "result-text")
print("Found text of Looks like a button")
time.sleep(3)

# Go to Disabled page
button_page = driver.find_element(By.LINK_TEXT, "Disabled")
button_page.click()
time.sleep(3)

# Select dropdown
select = Select(driver.find_element(By.ID, "id_select_state"))
drop_down = driver.find_element(By.ID, "id_select_state")
select_drop = Select(drop_down)
select.select_by_value("enabled")
time.sleep(3)

# Select dropdown button click
click_button = driver.find_element(By.ID, "submit-id-submit")
click_button.click()
time.sleep(3)
submitted_text_3 = driver.find_element(By.ID, "result-text")
print("Found text of dropdown")
time.sleep(3)








