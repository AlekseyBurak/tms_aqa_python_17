from selenium.webdriver.common.by import By


BN_offers = By.XPATH, '//span[@itemprop="offerCount"]'

SORT_OFFERS = By.XPATH, ('//*[@class="input-style input-style_more input-style_arrow_top-bottom input-style_base-alter '
                         'offers-list__input offers-list__input_width_auto offers-list__input_max-width_s"]')
SORTING_OFFERS = By.XPATH, '//*[@class="input-style__real"]'

BN_add_to_cart = By.XPATH, '(//a[@class="button-style button-style_base-alter offers-list__button offers-list__button_cart button-style_expletive"])[2]'
BN_go_to_cart = By.XPATH, '(//header[@class="g-top"]//a[@href="https://cart.onliner.by"])[1]'



TXT_price = By.XPATH, '(//div[@class="offers-list__description offers-list__description_alter-other offers-list__description_huge-alter offers-list__description_font-weight_bold offers-list__description_ellipsis offers-list__description_nodecor"])[1]'
