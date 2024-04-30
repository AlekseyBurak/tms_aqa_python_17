from selenium.webdriver.common.by import By

TXT_CART_PRICE = By.XPATH, '//div[contains(@class, "cart-form__offers-part_sum_clover")]'
BN_SUBMIT = By.XPATH, '//a[contains(text(), "Перейти к оформлению")]'