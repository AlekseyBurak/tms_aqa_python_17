import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def test_iframes(driver):
    driver.get("https://www.qa-practice.com/elements/iframe/iframe_page")
    iframe1 = driver.find_element(By.XPATH, "//*[@id='content']/iframe")
    driver.switch_to.frame(iframe1)
    action = ActionChains(driver)
    #main call to action button
    action.move_to_element(driver.find_element(By.XPATH, "//*[@class='btn btn-primary my-2']")).click()
    action.perform()

