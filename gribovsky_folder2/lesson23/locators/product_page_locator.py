from selenium.webdriver.common.by import By

BN_ADD_TO_CART = By.XPATH, '(//a[contains(@class, "product-aside__button_cart")])[1]'

BN_GO_TO_CART = (By.XPATH, '//*[contains(text(), "Перейти в корзину")]')

TXT_PRIMARY_PRICE = By.XPATH, '//div[contains(@class, "offers-description__price offers-description__price_primary")]'

