import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


# Alert
def test_alert_confirmation_box_accept(driver):
    url = "https://www.qa-practice.com/elements/alert/alert"
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/alert/confirm"]').click()
    driver.find_element(By.CLASS_NAME, "a-button").click()
    driver.switch_to.alert.accept()
    title = driver.find_element(By.XPATH, '//*[@id="result"]/p[1]')
    text = driver.find_element(By.XPATH, '//*[@id="result-text"]')
    assert title.text == 'You selected' and text.text == 'Ok'


def test_alert_confirmation_box_dismiss(driver):
    url = "https://www.qa-practice.com/elements/alert/alert"
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/alert/confirm"]').click()
    driver.find_element(By.CLASS_NAME, "a-button").click()
    driver.switch_to.alert.dismiss()
    title = driver.find_element(By.XPATH, '//*[@id="result"]/p[1]')
    text = driver.find_element(By.XPATH, '//*[@id="result-text"]')
    assert title.text == 'You selected' and text.text == 'Cancel'


def test_alert_prompt_box(driver):
    url = "https://www.qa-practice.com/elements/alert/prompt"
    driver.get(url)
    driver.find_element(By.CLASS_NAME, "a-button").click()
    alert = driver.switch_to.alert
    alert.send_keys('Hello')
    alert.accept()


# Iframe
def test_iframe(driver):
    url = "https://www.qa-practice.com/elements/iframe/iframe_page"
    driver.get(url)
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)

    driver.find_element(By.XPATH, '//*[@class="btn btn-primary my-2"]').click()
    # go back
    driver.switch_to.default_content()


# New tab
def test_new_tab(driver):  # ???
    url = "https://www.qa-practice.com/elements/new_tab/link"
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/new_tab"]').click()
    driver.find_element(By.XPATH, '//*[@href="/elements/new_tab/new_page"]').click()
    driver.switch_to.window(driver.window_handles[1])


# Drag and drop
def test_drag_and_drop_images(driver):
    url = "https://www.qa-practice.com/elements/dragndrop/images"
    driver.get(url)
    drag = driver.find_element(By.XPATH, '//div[@id="rect-droppable1"]/img')
    drop = driver.find_element(By.XPATH, '//div[@id="rect-droppable2"]')
    action = ActionChains(driver)
    action.move_to_element(drag).click_and_hold().move_to_element(drop).release(drag).perform()
    assert driver.find_element(By.XPATH, '//*[@id="rect-droppable2"]/p').text == 'Dropped!'


# Checkbox
def test_single_checkbox(driver):
    url = "https://www.qa-practice.com/elements/checkbox/single_checkbox"
    driver.get(url)
    driver.find_element(By.XPATH, '//input[@id = "id_checkbox_0"]').click()
    driver.find_element(By.ID, 'submit-id-submit').submit()



def test_multi_checkbox(driver):
    url = "https://www.qa-practice.com/elements/checkbox/mult_checkbox"
    driver.get(url)
    driver.find_element(By.XPATH, '//input[@id="id_checkboxes_0"]').click()
    driver.find_element(By.XPATH, '//input[@id="id_checkboxes_2"]').click()
    driver.find_element(By.ID, 'submit-id-submit').submit()



# Select
def test_single_select(driver):
    url = "https://www.qa-practice.com/elements/select/single_select"
    driver.get(url)
    Select(driver.find_element(By.XPATH, '//*[@name="choose_language"]')).select_by_visible_text("Java")
    driver.find_element(By.XPATH, '//*[@id="submit-id-submit"]').click()


def test_multi_select(driver):
    url = "https://www.qa-practice.com/elements/select/mult_select"
    driver.get(url)
    Select(driver.find_element(By.XPATH, '//*[@name="choose_the_place_you_want_to_go"]')).select_by_visible_text(
        "Ocean")
    Select(driver.find_element(By.XPATH, '//*[@name="choose_how_you_want_to_get_there"]')).select_by_visible_text(
        "Car")
    Select(driver.find_element(By.XPATH, '//*[@name="choose_when_you_want_to_go"]')).select_by_index(2)
    driver.find_element(By.XPATH, '//*[@id="submit-id-submit"]').click()


# Text area
def test_text_area(driver):
    url = "https://www.qa-practice.com/elements/textarea/single"
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@name="text_area"]').send_keys('Hello')
    driver.find_element(By.XPATH, '//*[@id="submit-id-submit"]').click()
