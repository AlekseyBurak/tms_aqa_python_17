# from selenium.webdriver.common.by import By
#
#
# def test_input(driver):
#     url = "https://www.qa-practice.com/elements/input/simple"
#     driver.get(url)
#     input_field = driver.find_element(By.ID, "id_text_string")
#     input_field.send_keys("HW example")
#     input_field.submit()
#
#
# def test_button(driver):
#     url = "https://www.qa-practice.com/elements/button/simple"
#     driver.get(url)
#     driver.find_element(By.ID, "submit-id-submit").click()
#     assert driver.find_element(By.ID, "result-text").text == "Submitted"
#
#
