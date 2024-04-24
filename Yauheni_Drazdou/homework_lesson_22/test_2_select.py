from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

def test_select(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    #Single select
    driver.find_element(By.XPATH, "//*[@href='/elements/select/single_select']").click()
    Select(driver.find_element(By.ID, "id_choose_language")).select_by_visible_text("Python")
    driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]').click()
    assert driver.find_element(By.ID, "result-text").text == "Python"

    #Multiply select
    driver.find_element(By.XPATH, "//*[@href='/elements/select/mult_select']").click()
    Select(driver.find_element(By.ID, "id_choose_the_place_you_want_to_go")).select_by_index(2)
    Select(driver.find_element(By.ID, "id_choose_how_you_want_to_get_there")).select_by_index(3)
    Select(driver.find_element(By.ID, "id_choose_when_you_want_to_go")).select_by_index(1)
    submit = driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]')
    action = ActionChains(driver)
    action.move_to_element(submit).click()
    action.perform()
    assert driver.find_element(By.ID, "result-text").text == "to go by train to the mountains today"