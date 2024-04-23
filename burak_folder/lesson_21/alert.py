import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()

# url = "https://www.qa-practice.com/elements/alert/alert"
# #
# #
# driver = webdriver.Chrome(options=chrome_options)
# driver.get(url)
# time.sleep(10)
# #
# driver.find_element(By.CLASS_NAME, "a-button").click()
# alert = driver.switch_to.alert
# time.sleep(2)
# alert.accept()
# time.sleep(2)

# url = "https://www.qa-practice.com/elements/alert/confirm"
#
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get(url)
# time.sleep(8)
#
# # Inputs
# driver.find_element(By.CLASS_NAME, "a-button").click()
# alert = driver.switch_to.alert
# time.sleep(2)
# alert.dismiss()
# time.sleep(5)

url = "https://www.qa-practice.com/elements/alert/prompt"


driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
time.sleep(8)
driver.find_element(By.CLASS_NAME, "a-button").click()
time.sleep(2)
alert = driver.switch_to.alert
time.sleep(2)
alert.send_keys("test")
time.sleep(2)

alert.accept()
time.sleep(5)