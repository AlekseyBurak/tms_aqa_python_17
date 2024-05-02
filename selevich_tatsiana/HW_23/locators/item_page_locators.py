from selenium.webdriver.common.by import By

BN_GO_TO_CART = By.XPATH, '//a[@class="button-style button-style_another button-style_base-alter product-recommended__button"]'

BN_ADD_TO_BUCKET = By.XPATH, '//a[contains(text(), "В корзину")]'

A_ITEM_PRICE = By.XPATH, '//a[@class="offers-description__link offers-description__link_nodecor js-description-price-link"]'
