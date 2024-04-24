from selenium.webdriver.common.by import By

def test_alert(driver):
    driver.get("https://www.qa-practice.com/elements/alert/alert")
    #aler box button
    driver.find_element(By.XPATH, "//*[@href='/elements/alert/alert']").click()
    driver.find_element(By.CLASS_NAME, "a-button").click()
    driver.switch_to.alert.accept()
    #confimation box button
    #cancel
    driver.find_element(By.XPATH, "//*[@href='/elements/alert/confirm']").click()
    driver.find_element(By.CLASS_NAME, "a-button").click()
    driver.switch_to.alert.dismiss()
    assert driver.find_element(By.ID, "result-text").text == "Cancel"
    driver.implicitly_wait(5)
    #ok
    driver.find_element(By.XPATH, "//*[@href='/elements/alert/confirm']").click()
    driver.find_element(By.CLASS_NAME, "a-button").click()
    driver.switch_to.alert.accept()
    assert driver.find_element(By.ID, "result-text").text == "Ok"
    #prompt box button
    #ok
    driver.find_element(By.XPATH, "//*[@href='/elements/alert/prompt']").click()
    driver.find_element(By.CLASS_NAME, "a-button").click()
    driver.switch_to.alert.send_keys("some text")
    driver.switch_to.alert.accept()
    assert driver.find_element(By.ID, "result-text").text == "some text"
    #cancel
    driver.find_element(By.XPATH, "//*[@href='/elements/alert/prompt']").click()
    driver.find_element(By.CLASS_NAME, "a-button").click()
    driver.switch_to.alert.send_keys("some text")
    driver.switch_to.alert.dismiss()
    assert driver.find_element(By.ID, "result-text").text == "You canceled the prompt"


