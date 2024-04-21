import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v121.indexed_db import Key
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.options import BaseOptions



driver = webdriver.Chrome()
driver.maximize_window()

print(driver.title)
print(driver.current_url)
class Inputs:
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_imbut = driver.find_element(By.ID, 'id_text_string')
    text_imbut.send_keys('text')
    text_imbut.submit()
    driver.find_element(By.LINK_TEXT, 'Email field').click()
    email_imput = driver.find_element(By.CSS_SELECTOR, '.textinput.textInput.form-control')
    email_imput.send_keys('re@rwe.com')
    email_imput.submit()
    driver.find_element(By.LINK_TEXT, 'Password field').click()
    password_imput = driver.find_element(By.XPATH, "//*[@type='password']")
    password_imput.send_keys("Password_123!")
    password_imput.submit()

class Buttons:
    driver.get('https://www.qa-practice.com/elements/button/simple')
    driver.find_element(By.ID, 'submit-id-submit').click()
    result_submit = driver.find_element(By.ID, 'result-text')
    print(result_submit.text)
    driver.find_element(By.LINK_TEXT, 'Looks like a button').click()
    driver.find_element(By.CSS_SELECTOR, '.a-button').click()
    result_submit = driver.find_element(By.ID, 'result-text')
    print(result_submit.text)
    driver.find_element(By.LINK_TEXT, 'Disabled').click()
    selection = Select(driver.find_element(By.ID, 'id_select_state'))

    selection.select_by_value('enabled')
    time.sleep(2)
    driver.find_element(By.ID, 'submit-id-submit').click()
    result_submit = driver.find_element(By.ID, 'result-text')
    print(result_submit.text)
