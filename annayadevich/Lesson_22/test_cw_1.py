from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_input(driver):
    url = "https://www.qa-practice.com/elements/input/simple"
    driver.get(url)
# Inputs
    input_field = driver.find_element(By.ID, "id_text_string")
    input_field.send_keys("HW example")
    input_field.submit()


def test_button(driver):
    url = "https://www.qa-practice.com/elements/button/simple"
    driver.get(url)
# # Go to buttons
#     driver.find_element(By.XPATH, "//*[@href='/elements/button']").click()
# # Simple button
    driver.find_element(By.ID, "submit-id-submit").click()
    assert driver.find_element(By.ID, "result-text").text == "Submitted"


def test_elements(driver):
    url = "https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html"
    driver.get(url)
    items = driver.find_elements(By.XPATH, '//*[@class="item product product-item"]')
    print(len(items))
    assert len(items) == 11
    for item in items:
        print()
        print(item.text)





# # Go to dropdown buttons
# driver.find_element(By.XPATH, "//*[@href='/elements/button/disabled']").click()
#
# # Disabled button
# drop_down = driver.find_element(By.ID, 'id_select_state')
# select = Select(drop_down)
# select.select_by_visible_text("Enabled")
# driver.find_element(By.ID, "submit-id-submit").click()
# assert driver.find_element(By.ID, "result-text").text == "Submitted"
