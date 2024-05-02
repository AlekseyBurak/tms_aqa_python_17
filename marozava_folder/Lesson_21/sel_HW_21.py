from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.qa-practice.com/elements/input/simple")
button = driver.find_element(By.XPATH, "//a[@href='/elements/button']")
button.click()
button_click = driver.find_element(By.ID, "submit-id-submit")
button_click.click()
disabled = driver.find_element(By.XPATH, "//a[@href='/elements/button/disabled']")
disabled.click()
enabled = driver.find_element(By.ID, "id_select_state")
select = Select(enabled)
select.select_by_index(1)
submit = driver.find_element(By.ID, "submit-id-submit")
submit.click()
inputs = driver.find_element(By.XPATH, "//a[@href='/elements/input']")
inputs.click()
text_inputs = driver.find_element(By.ID, "id_text_string")
text_inputs.send_keys("Marozava")
text_inputs.submit()
