
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


CURR_INFO = By.XPATH, '//span[@class="_u js-currency-amount"]'
class TestCurrency:

    def test_currency_info(self, driver):
        driver.get("https://www.onliner.by/")
        curr_info = WebDriverWait(driver, 10).until(EC.presence_of_element_located(CURR_INFO))

        assert "$" in curr_info.text
