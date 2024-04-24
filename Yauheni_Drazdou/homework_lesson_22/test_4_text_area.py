from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def test_text_area(driver):
    #text area button
    driver.get("https://www.qa-practice.com/elements/textarea/single")
    driver.find_element(By.XPATH, "//a[text()='Textarea']").click()
    driver.find_element(By.ID, "id_text_area").send_keys("Some text here")
    submit = driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]')
    driver.implicitly_wait(3)
    action = ActionChains(driver)
    action.move_to_element(submit).click()
    action.perform()
    assert driver.find_element(By.ID, "result-text").text == "Some text here"

    #multiply text areas button
    driver.find_element(By.XPATH, "//a[text()='Multiple textareas']").click()
    driver.find_element(By.ID, "id_first_chapter").send_keys("First")
    driver.find_element(By.ID, "id_second_chapter").send_keys("Second")
    driver.find_element(By.ID, "id_third_chapter").send_keys("Third")
    submit = driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]')
    driver.implicitly_wait(3)
    action = ActionChains(driver)
    action.move_to_element(submit).click()
    action.perform()
    assert driver.find_element(By.ID, "result-text").text == "First\nSecond\nThird"


