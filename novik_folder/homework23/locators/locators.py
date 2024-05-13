from selenium.webdriver.common.by import By

IN_SEARCH_FIELD = By.XPATH, '//input[@class="fast-search__input"]'

IFRAME = By.XPATH, '//iframe[@class="modal-iframe"]'

LI_SEARCH_RESULT = By.XPATH, '//li[@class="search__result"]'

LI_ITEM_SELLER = By.XPATH, '//*[@class="product-aside__offers-item product-aside__offers-item_primary"]'

LI_OVERFLOW = By.XPATH, '//*[@class = "product-recommended__sidebar-overflow"]'


BN_ADD = By.XPATH, '//*[@class="product-aside__offers-item product-aside__offers-item_primary"]//*[contains(@class, "product-aside__button_cart")]'

BN_NAV_TO = By.XPATH,'//*[@class = "product-recommended__sidebar-overflow"]//*[@class= "product-recommended__control product-recommended__control_checkout"]//*[@href="https://cart.onliner.by"]'

TXT_ITEM_IN_CART = By.XPATH, '//*[contains(@class, "cart-form__description_condensed-specific")]'