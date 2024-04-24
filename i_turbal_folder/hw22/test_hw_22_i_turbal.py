import time
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

url_input = 'https://www.qa-practice.com/elements/input/simple'
url_buttons = 'https://www.qa-practice.com/elements/button/simple'
url_checkboxes = 'https://www.qa-practice.com/elements/checkbox/single_checkbox'
url_alerts = 'https://www.qa-practice.com/elements/alert/alert'
url_drag_and_drops = 'https://www.qa-practice.com/elements/dragndrop/boxes'
url_iframes = 'https://www.qa-practice.com/elements/iframe/iframe_page'

def generation_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


class TestInptuts:

    def test_text_input_valid_case(self, driver):
        driver.get(url_input)
        text_input = driver.find_element(By.XPATH, "//*[@name='text_string']")
        valid_str = generation_string(5)
        text_input.send_keys(valid_str)
        text_input.submit()
        assert driver.find_element(By.XPATH, "//*[@class='result-text']").text == valid_str
        time.sleep(3)
    def test_text_input_invalid_case(self, driver):
        driver.get(url_input)
        text_input = driver.find_element(By.XPATH, "//*[@name='text_string']")
        invalid_str = generation_string(26)
        text_input.send_keys(invalid_str)
        text_input.submit()
        assert driver.find_element(By.XPATH, "//*[ @class ='invalid-feedback']").text == 'Please enter no more than 25 characters'

    def test_email_input_valid_case(self,driver):
        driver.get(url_input)
        driver.find_element(By.LINK_TEXT, 'Email field').click()
        email_input = driver.find_element(By.CSS_SELECTOR, '.textinput.textInput.form-control')
        valid_email = generation_string(5).lower()+'@test.com'
        email_input.send_keys(valid_email)
        email_input.submit()
        assert driver.find_element(By.XPATH, "//*[@class='result-text']").text == valid_email

    def test_email_input_invalid_case(self, driver):
        driver.get(url_input)
        driver.find_element(By.LINK_TEXT, 'Email field').click()
        email_input = driver.find_element(By.CSS_SELECTOR, '.textinput.textInput.form-control')
        email_input.send_keys(generation_string(5).lower())
        email_input.submit()
        assert driver.find_element(By.XPATH, "//*[ @class ='invalid-feedback']").text == 'Enter a valid email address.'


class TestButtons:
    def test_simple_button(self, driver):
        driver.get(url_buttons)
        driver.find_element(By.ID, 'submit-id-submit').click()
        assert driver.find_element(By.ID, 'result-text').text == "Submitted"
    def test_enabled(self, driver):
        driver.get(url_buttons)
        driver.find_element(By.LINK_TEXT, 'Disabled').click()
        selection = Select(driver.find_element(By.ID, 'id_select_state'))
        selection.select_by_value('enabled')
        driver.implicitly_wait(5)
        driver.find_element(By.ID, 'submit-id-submit').click()
        assert driver.find_element(By.ID, 'result-text').text == "Submitted"

class TestCheckboxes:

    def test_single_checkbox(self, driver):
        driver.get(url_checkboxes)
        driver.find_element(By.XPATH, "//*[@type='checkbox']").click()
        driver.find_element(By.CSS_SELECTOR, 'input.btn-primary').click()
        assert driver.find_element(By.XPATH, "//*[@class='result-text']").text == driver.find_element(By.CLASS_NAME, 'form-check-label').text.lower()

    def test_checkboxes_click_all(self, driver):
        driver.get(url_checkboxes)
        driver.find_element(By.XPATH, "//*[@id='content']/ul/li[2]").click()
        checkboxes = driver.find_elements(By.XPATH, "//*[@id='div_id_checkboxes']/div/div")
        for i in checkboxes:
            i.click()
        driver.find_element(By.ID, 'submit-id-submit').click()
        checkboxes_text = driver.find_elements(By.XPATH, "//*[@class='form-check-label']")
        cb_text = [cb.text for cb  in checkboxes_text]
        result = driver.find_element(By.ID, 'result-text')
        assert result.text == (', '.join(cb_text).lower())


#i've skipped tab "Select", cause it the same  my test "def test_enabled". they together are drop-downs
#i've skipped text area, tests will be equal as for inptuts

class TestAlerts:

    def test_alert(self,driver):
        driver.get(url_alerts)
        driver.find_element(By.CLASS_NAME, "a-button").click()
        alert = driver.switch_to.alert
        assert alert.text == 'I am an alert!'

    def test_confirmation(self, driver):
        driver.get(url_alerts)
        driver.find_element(By.LINK_TEXT, 'Confirmation box').click()
        driver.find_element(By.CLASS_NAME, "a-button").click()
        confirm = driver.switch_to.alert
        confirm.accept()
        assert driver.find_element(By.ID, 'result-text').text == 'Ok'
        # i know, that better write different test for  different  case, but i'm tired
        driver.find_element(By.CLASS_NAME, "a-button").click()
        alert = driver.switch_to.alert
        alert.dismiss()
        assert driver.find_element(By.ID, 'result-text').text == 'Cancel'

    def test_prompt(self,driver):
        driver.get(url_alerts)
        driver.find_element(By.LINK_TEXT, 'Prompt box').click()
        driver.find_element(By.CLASS_NAME, "a-button").click()
        prompt = driver.switch_to.alert
        new_string = generation_string(5)
        prompt.send_keys(new_string)
        prompt.accept()
        assert driver.find_element(By.ID, 'result-text').text == new_string






# class TestIframe:
#     def test_iframe(self,driver):
#         driver.get(url_iframes)
#         driver.implicitly_wait(5)
#         iframe = driver.find_element(By.TAG_NAME, 'iframe')
#         driver.switch_to.frame(iframe)
#         link = driver.find_element(By.XPATH, '//*[contains(text(), "Visit the homepage")]')
#         link.click()
#         assert







