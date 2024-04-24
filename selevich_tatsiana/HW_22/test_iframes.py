import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from urls import IFRAME_URL


@pytest.mark.url(IFRAME_URL)
class TestCaseIFrame:
    def test_iframe(self, driver):
        iframe = driver.find_element(By.TAG_NAME, 'iframe')
        driver.switch_to.frame(iframe)

        action = ActionChains(driver)

        link = driver.find_element(By.LINK_TEXT, 'Visit the homepage')
        action.scroll_to_element(link).perform()
        link.click()

        assert driver.find_element(By.XPATH, '//*[@id="content"]/div/h1').text == 'Hello!'
