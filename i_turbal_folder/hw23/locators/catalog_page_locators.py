from selenium.webdriver.common.by import By


BT_ONLINE_PRIME = By.XPATH, '//span[contains(text(), "Onlíner Prime")]'
BT_ZOO = By.XPATH, '//*[contains(text(),"Зоотовары")]'

BT_ZOO_HOUSES = By.XPATH, '//a[contains(@href,"pet_house")]'
CHB_FOR_CATS = By.XPATH, '(//div[@class="catalog-form__field"])[7]/div/ul/li[1]/label/div/div[1]'
TXT_OF_CHB_CATS = By.XPATH, '(//div[@class="catalog-form__field"])[7]/div/ul/li[1]/label/div/div[2]'

SL_WHERE = By.XPATH, '(//div[@class = "input-style__real"])[4]'
CHB_FLOOR = By.XPATH, '(//*[contains(@class, "dropdown-style__checkbox-sign")])[111]'

LINK_FIRST_ITEM = By.XPATH, '//div[contains(@class, "catalog-form__offers-list")]/div[1]/div/div/div'

