from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")

url = "https://www.qa-practice.com/elements/input/simple"


driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.get(url)

# Inputs
input_field = driver.find_element(By.ID, "id_text_string")
input_field.send_keys("HW example")
input_field.submit()

# Go to buttons
driver.find_element(By.XPATH, "//*[@href='/elements/button']").click()

# Simple button
driver.find_element(By.ID, "submit-id-submit").click()
assert driver.find_element(By.ID, "result-text").text == "Submitted"

# Go to dropdown buttons
driver.find_element(By.XPATH, "//*[@href='/elements/button/disabled']").click()

# Disabled button
drop_down = driver.find_element(By.ID, 'id_select_state')
select = Select(drop_down)
select.select_by_visible_text("Enabled")
driver.find_element(By.ID, "submit-id-submit").click()
assert driver.find_element(By.ID, "result-text").text == "Submitted"
