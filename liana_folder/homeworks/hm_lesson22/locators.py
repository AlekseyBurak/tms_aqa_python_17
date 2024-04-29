from selenium.webdriver.common.by import By

URL = "https://www.qa-practice.com/"
URL_SINGLE_CHECKBOX = "https://www.qa-practice.com/elements/checkbox/single_checkbox"
URL_MULT_CHECKBOXES = "https://www.qa-practice.com/elements/checkbox/mult_checkbox"
URL_SINGLE_SELECT = "https://www.qa-practice.com/elements/select/single_select"
URL_MULT_SELECT = "https://www.qa-practice.com/elements/select/mult_select"
URL_SINGLE_TEXT_AREA = "https://www.qa-practice.com/elements/textarea/single"


CH_SINGLE_CHECKBOX = By.XPATH, '//input[@id="id_checkbox_0"]'
# CH_SINGLE_CHECKBOX = '//input[@id="id_checkbox_0"]'
BN_SUBMIT = By.XPATH, '//input[@id="submit-id-submit"]'

CH_ONE_CHECKBOX = By.XPATH, '//input[@id="id_checkboxes_0"]'
CH_TWO_CHECKBOX = By.XPATH, '//input[@id="id_checkboxes_1"]'
CH_THREE_CHECKBOX = By.XPATH, '//input[@id="id_checkboxes_2"]'

SL_SINGLE_SELECT = By.XPATH, '//select[@id="id_choose_language"]'

TA_SINGLE_TEXT_AREA = By.XPATH, '//textarea[@id="id_text_area"]'
