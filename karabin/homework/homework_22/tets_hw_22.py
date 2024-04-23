import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


url = "https://www.qa-practice.com/elements/input/simple"


def test_checkbox_single(driver):
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/checkbox"]').click()
    driver.find_element(By.XPATH, '//*[@type="checkbox"]').submit()


def test_checkbox_some(driver):
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/checkbox"]').click()
    driver.find_element(By.XPATH, '//*[@href="/elements/checkbox/mult_checkbox"]').click()
    driver.find_element(By.XPATH, '//*[@id="id_checkboxes_0"]').submit()


def test_select_single(driver):
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/select"]').click()
    Select(driver.find_element(By.XPATH, '//*[@name="choose_language"]')).select_by_visible_text("Python")
    driver.find_element(By.XPATH, '//*[@id="submit-id-submit"]').click()


def test_select_multi(driver):
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/select"]').click()
    driver.find_element(By.XPATH, '//*[@href="/elements/select/mult_select"]').click()
    Select(driver.find_element(By.XPATH, '//*[@name="choose_the_place_you_want_to_go"]')).select_by_index(1)
    Select(driver.find_element(By.XPATH, '//*[@name="choose_how_you_want_to_get_there"]')).select_by_visible_text("Train")
    Select(driver.find_element(By.XPATH, '//*[@name="choose_when_you_want_to_go"]')).select_by_value("3")
    driver.find_element(By.XPATH, '//*[@id="submit-id-submit"]').click()


def test_new_tab_link(driver):
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/new_tab"]').click()


def test_new_tab_button(driver):
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/new_tab"]').click()
    driver.find_element(By.XPATH, '//*[@href="/elements/new_tab/new_page"]').click()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH, '//*[@href="/elements/new_tab/button"]').click()
    driver.find_element(By.XPATH, '//*[@href="/elements/new_tab/new_page"]').click()


def test_text_area(driver):
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/textarea"]').click()
    driver.find_element(By.XPATH, '//*[@href="/elements/textarea/single"]').click()
    driver.find_element(By.XPATH, '//*[@name="text_area"]').send_keys('I\n did\n it\n')
    driver.find_element(By.XPATH, '//*[@id="submit-id-submit"]').click()


def test_multiple_text_area(driver):
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/textarea"]').click()
    driver.find_element(By.XPATH, '//*[@href="/elements/textarea/textareas"]').click()
    driver.find_element(By.XPATH, '//*[@name="first_chapter"]').send_keys('I')
    driver.find_element(By.XPATH, '//*[@name="second_chapter"]').send_keys('like to')
    driver.find_element(By.XPATH, '//*[@name="third_chapter"]').send_keys('test')
    ActionChains(driver).scroll_to_element(driver.find_element(By.XPATH, '//*[@id="submit-id-submit"]')).perform()


def test_alert_box(driver):
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href = "/elements/alert"]').click()
    driver.find_element(By.XPATH, '//*[@href="#"]').click()
    driver.switch_to.alert.accept()
    time.sleep(3)


def test_alert_confirmation_box(driver):
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href = "/elements/alert"]').click()
    driver.find_element(By.XPATH, '//*[@href="/elements/alert/confirm"]').click()
    driver.find_element(By.XPATH, '//*[@href = "#"]').click()
    driver.switch_to.alert.dismiss()


def test_alert_prompt_box(driver):
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href = "/elements/alert"]').click()
    driver.find_element(By.XPATH, '//*[@href="/elements/alert/prompt"]').click()
    driver.find_element(By.XPATH, '//*[@class="a-button"]').click()
    driver.switch_to.alert.send_keys("I am an alert!")
    driver.switch_to.alert.accept()


def test_drag_n_drop_boxes(driver):
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/dragndrop"]').click()
    ActionChains(driver).drag_and_drop(driver.find_element(By.XPATH, '//*[@id="rect-draggable"]'),
                                       driver.find_element(By.XPATH, '//*[@id="rect-droppable"]')).perform()


def test_drag_n_drop_images(driver):
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href="/elements/dragndrop"]').click()
    driver.find_element(By.XPATH, '//*[@href="/elements/dragndrop/images"]').click()
    ActionChains(driver).drag_and_drop(driver.find_element(By.XPATH, '//*[@src="/static/home/smile.png"]'),
                                       driver.find_element(By.XPATH, '//*[@id="rect-droppable2"]')).perform()


def test_iframe(driver):
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@href = "/elements/iframe/iframe_page"]').click()
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
    driver.find_element(By.XPATH, '//*[@class="btn btn-primary my-2"]').click()
    driver.switch_to.default_content()
