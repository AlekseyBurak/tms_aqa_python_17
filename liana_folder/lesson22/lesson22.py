import selenium
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# def test_input(driver):
#     driver.get(url)
#     text_field = driver.find_element(By.ID, "id_text_string")
#     text_field.send_keys("Lorem ipsum dolor sit amet")
#     text_field.submit()
#
#
# def test_button(driver):
#     driver.get(url)
#     driver.find_element(By.LINK_TEXT, "Buttons").click()
#     driver.find_element(By.ID, "submit-id-submit").click()
#     assert driver.find_element(By.ID, "result-text").text == "Submitted"
#
#
# def test_elements(driver):
#     url_magento = "https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html"
#     driver.get(url_magento)
#     items = driver.find_elements(By.XPATH, '//*[@class="item product product-item"]')
#     print(len(items))
#     assert len(items) == 11
#     for item in items:
#         print()
#         print(item.text)

def test_elements(driver):
    url = "https://www.qa-practice.com/elements/alert/alert"
    driver.get(url)
