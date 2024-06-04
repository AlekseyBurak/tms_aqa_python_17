from selenium.webdriver.common.by import By

CURR_INFO = By.XPATH, '//span[@class="_u js-currency-amount"]'

IN_SEARCH_FIELD = By.XPATH, '//input[@class="fast-search__input"]'

IFRAME = By.XPATH, '//iframe[@class="modal-iframe"]'

LI_SEARCH_RESULT = By.XPATH, '(//li[contains(@class, "search__result")])'

CONSENT_BUTTON = By.XPATH, '//button[@class="fc-button fc-cta-consent fc-primary-button"]'

LI_BASKET = By.LINK_TEXT, "В корзину"

INITIAL_PRICE = By.XPATH, '//a[@class="product-aside__link product-aside__link_alter-other ' \
                  'product-aside__link_font-weight_bold product-aside__link_ellipsis product-aside__link_nodecor ' \
                  'js-short-price-link product-aside__link_huge-additional"]//span'

GO_TO_BASKET = By.XPATH, '//a[@class="button-style button-style_another button-style_base-alter ' \
                         'product-recommended__button"]'

BASKET_PRICE = By.XPATH, '//div[@class="cart-form__offers-part cart-form__offers-part_total"]//div[' \
                         '@class="cart-form__description cart-form__description_base-alter ' \
                         'cart-form__description_font-weight_semibold cart-form__description_ellipsis ' \
                         'cart-form__description_condensed"]//span'

BU_CHECKOUT = By.XPATH, '//a[@class="button-style button-style_small cart-form__button button-style_primary"]'
