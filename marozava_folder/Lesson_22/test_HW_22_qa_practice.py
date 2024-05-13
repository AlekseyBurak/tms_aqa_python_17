from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time


def test_checkbox_single(driver):
    url = "https://www.qa-practice.com/elements/input/simple"
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/checkbox"]').click()
    driver.find_element(By.XPATH, '//*[@type="checkbox"]').click()
    driver.find_element(By.XPATH, '//*[@id="submit-id-submit"]').click()
    assert driver.find_element(By.XPATH, '//*[@class="result-text"]').text == 'select me or not'


def test_checkboxes(driver):
    url = "https://www.qa-practice.com/elements/input/simple"
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/checkbox"]').click()
    driver.find_element(By.XPATH, '//*[@href="/elements/checkbox/mult_checkbox"]').click()
    driver.find_element(By.XPATH, '//*[@id="id_checkboxes_0"]').click()
    driver.find_element(By.XPATH, '//*[@id="id_checkboxes_1"]').click()
    driver.find_element(By.XPATH, '//*[@id="id_checkboxes_2"]').click()
    driver.find_element(By.XPATH, '//*[@id="submit-id-submit"]').click()
    assert driver.find_element(By.XPATH, '//*[@id="result-text"]').text == 'one, two, three'


def test_select(driver):
    url = "https://www.qa-practice.com/elements/input/simple"
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/select"]').click()
    Select(driver.find_element(By.XPATH, '//*[@name="choose_language"]')).select_by_visible_text("Java")
    driver.find_element(By.XPATH, '//*[@id="submit-id-submit"]').click()
    assert driver.find_element(By.XPATH, '//*[@id="result-text"]').text == 'Java'


def test_new_tab_link(driver):
    url = "https://www.qa-practice.com/elements/input/simple"
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/new_tab"]').click()
    driver.find_element(By.XPATH, '//*[@href="/elements/new_tab/new_page"]').click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.find_element(By.XPATH, '//*[@id="result-text"]').text == 'I am a new page in a new tab'


def test_text_area(driver):
    url = "https://www.qa-practice.com/elements/input/simple"
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/textarea"]').click()
    driver.find_element(By.XPATH, '//*[@href="/elements/textarea/single"]').click()
    driver.find_element(By.XPATH, '//*[@name="text_area"]').send_keys('I am happy')
    driver.find_element(By.XPATH, '//*[@id="submit-id-submit"]').click()
    assert driver.find_element(By.XPATH, '//*[@class="result-chapters"]').text == 'I am happy'


def test_alert(driver):
    url = "https://www.qa-practice.com/elements/input/simple"
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href = "/elements/alert"]').click()
    driver.find_element(By.XPATH, '//*[@href="#"]').click()
    driver.switch_to.alert.accept()


def test_dragndrop_boxes(driver):
    url = "https://www.qa-practice.com/elements/input/simple"
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/dragndrop"]').click()
    ActionChains(driver).drag_and_drop(driver.find_element(By.XPATH, '//*[@id="rect-draggable"]'),
                                       driver.find_element(By.XPATH, '//*[@id="rect-droppable"]')).perform()


def test_dragndrop_images(driver):
    url = "https://www.qa-practice.com/elements/input/simple"
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/dragndrop"]').click()
    driver.find_element(By.XPATH, '//*[@href="/elements/dragndrop/images"]').click()
    ActionChains(driver).drag_and_drop(driver.find_element(By.XPATH, '//*[@src="/static/home/smile.png"]'),
                                       driver.find_element(By.XPATH, '//*[@id="rect-droppable2"]')).perform()
