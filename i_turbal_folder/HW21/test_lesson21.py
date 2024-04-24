import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


url_input = 'https://www.qa-practice.com/elements/input/'


def test_input(driver):
    driver.get(url_input)
    text_imbut = driver.find_element(By.ID, 'id_text_string')
    text_imbut.send_keys('text')
    text_imbut.submit()

def test_button(driver):
    driver.get('https://www.qa-practice.com/elements/button/simple')
    driver.find_element(By.ID, 'submit-id-submit').click()
    result_submit = driver.find_element(By.ID, 'result-text').text
    assert result_submit == "Submitted"


def test_elements(driver):
    driver.get('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
    items = driver.find_elements(By.XPATH, '//*[@class="item product product-item"]')
    assert len(items) == 11


def test_alert(driver):
    url = 'https://www.qa-practice.com/elements/alert/confirm'
    driver.get(url)
    driver.find_element(By.CLASS_NAME, "a-button").click()
    alert = driver.switch_to.alert
    time.sleep(2)
    alert.dismiss()
    time.sleep(2)


def test_iframe(driver):
    url = "https://www.qa-practice.com/elements/iframe/iframe_page"
    time.sleep(5)
    driver.get(url)
    time.sleep(2)
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@class="btn btn-primary my-2"]').click()

    # go back
    driver.switch_to.default_content()

def test_action_chains(driver):
    url = "https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html"
    time.sleep(5)
    driver.get(url)
    time.sleep(2)
    card = driver.find_element(By.XPATH, '//*[@class="item product product-item"][2]')
    button = driver.find_element(By.XPATH, '//*[@title="Add to Cart"]')
    action = ActionChains(driver)
    (action.move_to_element(card).
     move_to_element(button).
     click(button).
     perform())
    time.sleep(10)

def test_js(driver):
    url = "https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html"
    time.sleep(5)
    driver.get(url)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # driver.execute_script("arguments[0].click();", element)
    time.sleep(3)

def test_drag_and_drop(driver):
    url = "https://www.qa-practice.com/elements/dragndrop/boxes"
    time.sleep(5)
    driver.get(url)
    time.sleep(2)
    drag = driver.find_element(By.ID, 'rect-draggable')
    drop = driver.find_element(By.ID, 'rect-droppable')
    action = ActionChains(driver)
    (action.drag_and_drop(drag, drop).perform())
    time.sleep(10)

def test_drag_and_drop_2(driver):
    url = "https://www.qa-practice.com/elements/dragndrop/boxes"
    time.sleep(5)
    driver.get(url)
    time.sleep(2)
    drag = driver.find_element(By.ID, 'rect-draggable')
    drop = driver.find_element(By.ID, 'rect-droppable')
    action = ActionChains(driver)
    # (action.drag_and_drop(drag, drop).perform())
    action.move_to_element(drag).click_and_hold().move_to_element(drop).release(drag).perform()
    time.sleep(10)
