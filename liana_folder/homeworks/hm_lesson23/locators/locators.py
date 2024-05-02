from selenium.webdriver.common.by import By

IN_SEARCH_FIELD = By.XPATH, '//input[@class="fast-search__input"]'
IFRAME = By.XPATH, '//iframe[@class="modal-iframe"]'
SEARCH_RESULT = By.XPATH, '//li[@class="search__result"]'
HEADER = By.XPATH, '//div[@class="catalog-masthead"]/h1'
BT_ADD_TO_CART = By.XPATH, '//div[@class="product-aside__control product-aside__control_condensed-additional"]'
SIDEBAR = By.XPATH, '//div[@class="product-recommended__sidebar-overflow"]'
BN_GO_TO_CART = By.XPATH, '//a[@href="https://cart.onliner.by"][contains(text(), "Перейти в корзину")]'
BN_ACCEPT = By.XPATH, '//p[contains(text(), "Соглашаюсь")]'
BN_GO_TO_CHECKOUT = By.XPATH, '//a[contains(text(), "Перейти к оформлению")]'
HEADER_CHECKOUT = By.XPATH, '//*[contains(text(), "Оформление заказа")]'