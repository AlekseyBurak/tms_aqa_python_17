from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome()

url = https://www.qa-practice.com/elements/input/simple
driver.get("http://www.google.com")

element = WebDriverWait(driver,10).until(EC.presence_of_element_located(By.XPATH. ))
