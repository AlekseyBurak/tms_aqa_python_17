import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


# test checkboxes
def test_checkbox(driver):
    url = "https://www.qa-practice.com/elements/checkbox/single_checkbox"
    driver.get(url)
    driver.find_element(By.ID, "id_checkbox_0").click()
    driver.find_element(By.ID, "submit-id-submit").click()
    assert driver.find_element(By.CLASS_NAME, "result").text == "Selected checkboxes:\nselect me or not"

# test select
def test_select(driver):
    url = "https://www.qa-practice.com/elements/select/single_select"
    driver.get(url)
    select = Select(driver.find_element(By.CLASS_NAME, "form-select"))
    select.select_by_visible_text("Python")
    driver.find_element(By.ID, "submit-id-submit").click()
    assert driver.find_element(By.CLASS_NAME, "result").text == "You selected\nPython"

# test text_area
def test_text_area(driver):
    url = "https://www.qa-practice.com/elements/textarea/single"
    driver.get(url)
    driver.find_element(By.ID, "id_text_area").send_keys("hello")
    driver.find_element(By.ID, "submit-id-submit").click()
    assert driver.find_element(By.ID, "result").text == "You entered\nhello"

# test alers
def test_alerts(driver):
    url = "https://www.qa-practice.com/elements/alert/confirm"
    driver.get(url)
    driver.find_element(By.CLASS_NAME, "a-button").click()
    alert = driver.switch_to.alert
    alert.accept()
    assert driver.find_element(By.ID, "result").text == "You selected\nOk"