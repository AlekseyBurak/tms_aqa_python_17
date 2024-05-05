from selenium.webdriver.common.by import By

PRICE = By.XPATH, "//div[@class='product-aside__offers-list']/div[1]/div[1]/div[1]"
BT_BUY_NOW = By.XPATH, "//div[@class='product-aside__offers-list']/div[1]/div[4]/a[1]"
TOT_PRICE = By.XPATH, "//div[2]/div/div/div/div[2]/span"

TXT_ANIMAIL_TYPE = By.XPATH, '(//span[@class="value__text"])[2]'
TXT_PLACING_TYPE = By.XPATH, '(//span[@class="value__text"])[3]'