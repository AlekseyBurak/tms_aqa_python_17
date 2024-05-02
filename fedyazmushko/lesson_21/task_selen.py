import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.qa-practice.com/elements/input/simple")
# time.sleep(10)