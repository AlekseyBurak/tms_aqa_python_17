import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.qa-practice.com/elements/input/simple")

#заходит в инпут, вводит текст и затем удаляет его
input_fields = driver.find_element(By.NAME, "text_string")
input_fields.send_keys("Hello")
time.sleep(4)
input_fields.clear()
time.sleep(2)

#заходит в меню баттонс нажимает на кнопку клик и находит там сабмитед
button_menu_item = driver.find_element(By.LINK_TEXT, "Buttons")
button_menu_item.click()
time.sleep(2)
button_on_the_page = driver.find_element(By.NAME, "submit")
button_on_the_page.click()
time.sleep(2)
submitted_text = driver.find_element(By.ID, "result")
print(submitted_text.is_displayed())

#заходит в меню баттонс-> Disabled
# там выпадающий список в нем выбирает enabled => нажимает на кнопку => находит текст  submitted

disabled_menu_item = driver.find_element(By.LINK_TEXT, "Disabled")
disabled_menu_item.click()
time.sleep(2)
drop_down = driver.find_element(By.ID, "id_select_state")
select = Select(drop_down)
select.select_by_index(1)
time.sleep(2)
button_on_the_page_2 = driver.find_element(By.ID, "submit-id-submit")
button_on_the_page_2.click()
time.sleep(3)
submitted_text_1 = driver.find_element(By.ID, "result")
print(submitted_text_1.is_displayed())
