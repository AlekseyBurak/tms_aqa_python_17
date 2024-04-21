import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.qa-practice.com")


element_UI = driver.find_element(By.XPATH, '//*[contains(text(),"Single UI Elements")]')
element_UI.click()

"""email input"""
# element_Inputs = driver.find_element(By.XPATH, '//*[@href ="/elements/input"]')
# element_Inputs.click()
# email_field = driver.find_element(By.PARTIAL_LINK_TEXT, "Email")
# email_field.click()
# input_field = driver.find_element(By.NAME, "email")
# input_field.send_keys("gm81@tut.by")
# input_field.submit()
# time.sleep(5)

"""Simple button"""
# element_Buttons = driver.find_element(By.XPATH, '//*[@href ="/elements/button"]')
# time.sleep(1)
# element_Buttons.click()
# click_Button = driver.find_element(By.XPATH, '//*[@name="submit"]')
# click_Button.click()
# result = driver.find_element(By.XPATH, '//*[@name="result"]')
# time.sleep(1)
# print(result.is_displayed())

"""Disabled"""
# element_Buttons = driver.find_element(By.XPATH, '//*[@href ="/elements/button"]')
# time.sleep(1)
# element_Buttons.click()
# element_Disabled = driver.find_element(By.XPATH, '//*[@href ="/elements/button/disabled"]')
# time.sleep(1)
# element_Disabled.click()
# time.sleep(2)
# drop_down = driver.find_element(By.XPATH, '//*[@name="select_state"]')
# select = Select(drop_down)
# select.select_by_index(1)
# time.sleep(1)
# submit_Button = driver.find_element(By.NAME, "submit")
# submit_Button.click()
# result_2 = driver.find_element(By.XPATH, '//*[@name="result"]')
# print(result_2.is_displayed())
# time.sleep(3)



