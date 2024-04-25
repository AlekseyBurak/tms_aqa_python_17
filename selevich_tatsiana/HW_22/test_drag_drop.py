import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from urls import DRAG_DROP_BOXES_URL, DRAG_DROP_IMAGES_URL


@pytest.mark.url(DRAG_DROP_BOXES_URL)
class TestCaseDragDropBoxes:
    def test_drag_drop_box(self, driver):
        drag = driver.find_element(By.XPATH, '//div[@id="rect-draggable"]')
        drop = driver.find_element(By.XPATH, '//p[@id="text-droppable"]')

        action = ActionChains(driver)
        action.move_to_element(drag).click_and_hold().move_to_element(drop).release(drag).perform()

        assert driver.find_element(By.XPATH, '//*[@id="text-droppable"]').text == 'Dropped!'


@pytest.mark.url(DRAG_DROP_IMAGES_URL)
class TestCaseDragDropImages:
    def test_drag_drop_image(self, driver):
        drag = driver.find_element(By.XPATH, '//div[@id="rect-droppable1"]/img')
        drop = driver.find_element(By.XPATH, '//div[@id="rect-droppable2"]')

        action = ActionChains(driver)
        action.move_to_element(drag).click_and_hold().move_to_element(drop).release(drag).perform()

        assert driver.find_element(By.XPATH, '//*[@id="rect-droppable2"]/p').text == 'Dropped!'
