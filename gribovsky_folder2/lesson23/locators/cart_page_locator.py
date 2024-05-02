from selenium.webdriver.common.by import By

TXT_PRODUCT_CART_PRICE = By.XPATH, '//div[contains(@class, "cart-form__offers-part_sum_specific")]'
BN_SUBMIT_ORDER = By.XPATH, '//*[contains(text(), "Перейти к оформлению")]'
TXT_PRODUCT_CART_AMOUNT = By.XPATH, '//input[contains(@class, "input-style_text_center")]'  # не сработало
