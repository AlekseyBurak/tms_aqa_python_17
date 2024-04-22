import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.qa-practice.com/elements/input/simple")
driver.find_element(By.LINK_TEXT, "Buttons").click()
driver.find_element(By.LINK_TEXT, "Looks like a button").click()
driver.find_element(By.LINK_TEXT, "Disabled").click()
driver.find_element(By.NAME, "select_state").click()
Select(driver.find_element(By.NAME, "select_state")).select_by_value("enabled")
driver.find_element(By.NAME, "submit").click()
driver.get("https://www.qa-practice.com/elements/input/simple")
driver.find_element(By.LINK_TEXT, "Inputs").click()
driver.find_element(By.LINK_TEXT, "Text input").click()
driver.find_element(By.LINK_TEXT, "Email field").click()
driver.find_element(By.LINK_TEXT, "Password field").click()
driver.find_element(By.NAME, "password").send_keys("Qwer!123\n")

