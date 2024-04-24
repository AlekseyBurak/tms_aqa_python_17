import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v121.indexed_db import Key
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.options import BaseOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome
driver.get("https://www.google.com/")
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@name="btnK"]')
    )
)
# driver.implicitly_wait(5) не явное ожидание - одновремно исполь
