from selenium.webdriver.common.by import By

def test_new_tab(driver):
    # new tab link
    driver.get("https://www.qa-practice.com/elements/new_tab/link")
    driver.find_element(By.ID, "new-page-link").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(3)
    assert driver.current_url == "https://www.qa-practice.com/elements/new_tab/new_page"
    assert driver.find_element(By.ID, "result-text").text == "I am a new page in a new tab"

    # new tab button
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, "//*[@href='/elements/new_tab/button']").click()
    driver.find_element(By.ID, "new-page-button").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(3)
    assert driver.current_url == "https://www.qa-practice.com/elements/new_tab/new_page"
    assert driver.find_element(By.ID, "result-text").text == "I am a new page in a new tab"





