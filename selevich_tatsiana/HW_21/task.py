from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

URL = "https://www.qa-practice.com/elements/input/simple"


class TaskChromeNavigator:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)

    def submit_input_field_by_id(self, field_id, input_value):
        input_field = self.driver.find_element(By.ID, field_id)
        input_field.send_keys(input_value)
        input_field.submit()

    def check_submit_button_result(self, button_locator, button_locator_value):
        button = self.driver.find_element(button_locator, button_locator_value)
        button.submit()

        element = self.driver.find_element(By.ID, "result-text")
        text = element.text

        if text == "Submitted":
            print("Yeah")

    def navigate_to_tab_by_link_text(self, tab_locator_value):
        tab = self.driver.find_element(By.LINK_TEXT, tab_locator_value)
        tab.click()

    def select_dropdown_value_by_id(self, dropdown_id, selected_field_value):
        drop_down = self.driver.find_element(By.ID, dropdown_id)
        select = Select(drop_down)
        select.select_by_value(selected_field_value)

    def navigate_by_site(self):
        self.submit_input_field_by_id("id_text_string", "Hello")

        self.navigate_to_tab_by_link_text("Email field")
        self.submit_input_field_by_id("id_email", "hey@gmail.com")

        self.navigate_to_tab_by_link_text("Password field")
        self.submit_input_field_by_id("id_password", "Qwerty1$")

        self.navigate_to_tab_by_link_text("Buttons")
        self.check_submit_button_result(By.ID, "submit-id-submit")

        self.navigate_to_tab_by_link_text("Looks like a button")
        self.check_submit_button_result(By.LINK_TEXT, "Click")

        self.navigate_to_tab_by_link_text("Disabled")
        self.select_dropdown_value_by_id("id_select_state", "enabled")
        self.check_submit_button_result(By.ID, "submit-id-submit")


navigator = TaskChromeNavigator()
navigator.navigate_by_site()
