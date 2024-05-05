import allure

from i_turbal_folder.hw23.locators.catalog_page_locators import BT_ONLINE_PRIME, BT_ZOO, BT_ZOO_HOUSES, CHB_FOR_CATS, \
    SL_WHERE, CHB_FLOOR, TXT_OF_CHB_CATS, LINK_FIRST_ITEM
from i_turbal_folder.hw23.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class CatalogPage(BasePage):

    @property
    def zoo(self):
        return self.wait_for(BT_ZOO)

    @property
    def zoo_house(self):
        return self.wait_for(BT_ZOO_HOUSES)

    @property
    def label_category_for_cat(self):
        return self.driver.find_element(*TXT_OF_CHB_CATS)
    @property
    def checkbox_cat(self):
        return self.driver.find_element(*CHB_FOR_CATS)

    def get_text_of_cat_category(self):
        return self.label_category_for_cat.text

    def select_category_for_cat(self):
        with allure.step("Select cat category"):
            self.driver.execute_script('arguments[0].click()', self.checkbox_cat)
            # action = ActionChains(self.driver)
            # action.move_to_element(self.checkbox_cat).perform()
            # action.click().perform()



    @property
    def find_selector_where(self):
        return self.driver.find_element(*SL_WHERE)

    @property
    def find_checbox_floor(self):
        return self.driver.find_element(*CHB_FLOOR)

    def open_selector_where(self):
        with allure.step("Open 'Размещение' drop-down filter"):
            self.driver.execute_script('arguments[0].click()', self.find_selector_where)
            # action = ActionChains(self.driver)
            # action.move_to_element(self.find_selector_where).perform()
            # action.click()

    def get_text_of_checbox_floor(self):
        return self.find_checbox_floor.text
    def select_checkbox_floor(self):
        with allure.step('Click the "Наполньое" checkbox'):
            self.driver.execute_script('arguments[0].click()', self.find_checbox_floor)
            # action = ActionChains(self.driver)
            # action.move_to_element(self.find_checbox_floor).perform()
            # action.click()
    def click_onliner_prime(self):
        with allure.step('Go to Online Prime page'):
            self.click(BT_ONLINE_PRIME)

    def go_to_zoo(self):
        with allure.step("Go to zoo category"):
            action = ActionChains(self.driver)
            action.move_to_element(self.zoo).perform()
        with allure.step("Open zoo houses"):
            action.move_to_element(self.zoo_house).perform()
            action.click().perform()

    def open_first_item(self):
        with allure.step('Open first item'):
            self.click(LINK_FIRST_ITEM)
