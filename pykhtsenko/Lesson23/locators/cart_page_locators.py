from selenium.webdriver.common.by import By


CURR_INFO = By.XPATH, '//span[@class="_u js-currency-amount"]'
IN_SEARCH_FIELD = By.XPATH, '//input[@class="fast-search__input"]'


IFRAME = By.XPATH, '//iframe[@class="modal-iframe"]'


LI_SEARCH_RESULT_FOR_INDEX = By.XPATH, '(//li[contains(@class, "search__result")])'

BN_CATALOG = By.XPATH, '(//a[@href="https://catalog.onliner.by"])[2]'