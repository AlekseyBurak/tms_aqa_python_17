# доработаю к четвергу
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.qa-practice.com/elements/input/simple")

element = driver.find_element(By.NAME, "Text input")
element.send_keys("Yana")
print(element)
element_2 = driver.find_element(By.NAME, "Email field")
element_2.send_keys("yana.pykhtsenko@gmail.com")
print(element_2)
element_3 = driver.find_element(By.NAME, "Password field")
element_3.send_keys("yana.pykhtsenko@gmail.com")
print(element_3)
driver.quit()

# click the button
driver = webdriver.Chrome()
driver.get("https://www.qa-practice.com/elements/input/simple")
button_element = driver.find_element(By.ID,"content")
button_element.click()
driver.quit()

# dropdown list
driver = webdriver.Chrome()
driver.get("https://www.qa-practice.com/elements/input/simple")
disabled_tab = driver.find_element(By.CLASS_NAME, "tab active")
disabled_tab.click()
dropdown = Select(driver.find_element_by_name("dropdown_list"))
dropdown.select_by_visible_text("Enabled")
submit_button = driver.find_element_by_id("submit_button")
submit_button.click()
submitted_text = driver.find_element_by_id("submitted_text").text
print(submitted_text)
driver.quit()