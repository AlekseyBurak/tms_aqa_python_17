from liana_folder.lesson23.pages.base_page import BasePage
from liana_folder.homeworks.hm_lesson23.locators.locators import HEADER_CHECKOUT


class CheckoutDetails(BasePage):

    @property
    def get_title(self):
        self.wait_for(HEADER_CHECKOUT)
        title = self.driver.find_element(*HEADER_CHECKOUT)
        return title.text






