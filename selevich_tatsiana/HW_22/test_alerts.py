import pytest
from selenium.webdriver.common.by import By
from urls import ALERT_BOX_URL, ALERT_CONFIRM_BOX_URL, ALERT_PROMPT_BOX_URL


@pytest.mark.url(ALERT_BOX_URL)
class TestCaseAlertBox:
    def test_text_alert_box(self, driver):
        driver.find_element(By.XPATH, '//*[@id="content"]/a[1]').click()
        alert = driver.switch_to.alert

        assert alert.text == 'I am an alert!'


@pytest.mark.url(ALERT_CONFIRM_BOX_URL)
class TestCaseAlertConfirmBox:
    def test_accept_alert_confirm_box(self, driver):
        driver.find_element(By.XPATH, '//*[@id="content"]/a[1]').click()
        driver.switch_to.alert.accept()

        title = driver.find_element(By.XPATH, '//*[@id="result"]/p[1]')
        text = driver.find_element(By.XPATH, '//*[@id="result-text"]')

        assert title.text == 'You selected' and text.text == 'Ok'

    def test_decline_alert_confirm_box(self, driver):
        driver.find_element(By.XPATH, '//*[@id="content"]/a[1]').click()
        driver.switch_to.alert.dismiss()

        title = driver.find_element(By.XPATH, '//*[@id="result"]/p[1]')
        text = driver.find_element(By.XPATH, '//*[@id="result-text"]')

        assert title.text == 'You selected' and text.text == 'Cancel'


@pytest.mark.url(ALERT_PROMPT_BOX_URL)
class TestCaseAlertPromptBox:
    def test_accept_alert_prompt_box(self, driver):
        driver.find_element(By.XPATH, '//*[@id="content"]/a[1]').click()
        alert = driver.switch_to.alert
        alert.send_keys('Text')
        alert.accept()

        title = driver.find_element(By.XPATH, '//*[@id="result-head"]')
        text = driver.find_element(By.XPATH, '//*[@id="result-text"]')

        assert title.text == 'You entered' and text.text == 'Text'

    def test_decline_alert_prompt_box(self, driver):
        driver.find_element(By.XPATH, '//*[@id="content"]/a[1]').click()
        driver.switch_to.alert.dismiss()

        text = driver.find_element(By.XPATH, '//*[@id="result-text"]')

        assert text.text == 'You canceled the prompt'

    def test_empty_accept_alert_prompt_box(self, driver):
        driver.find_element(By.XPATH, '//*[@id="content"]/a[1]').click()
        driver.switch_to.alert.accept()

        text = driver.find_element(By.XPATH, '//*[@id="result-text"]')

        assert text.text == 'You entered nothing'
