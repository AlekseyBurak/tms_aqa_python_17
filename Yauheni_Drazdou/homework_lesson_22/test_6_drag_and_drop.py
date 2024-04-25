from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def test_drag_drop(driver):
    # boxes button
    driver.get("https://www.qa-practice.com/elements/dragndrop/boxes")
    action = ActionChains(driver)
    drag = driver.find_element(By.ID, "rect-draggable")
    drop = driver.find_element(By.ID, "rect-droppable")
    action.drag_and_drop(drag, drop).perform()
    assert driver.find_element(By.ID, "text-droppable").text == "Dropped!"

    #images button
    driver.find_element(By.XPATH, "//*[@href='/elements/dragndrop/images']").click()
    action = ActionChains(driver)
    drag_smile = driver.find_element(By.ID, "rect-droppable1")
    dropbox = driver.find_element(By.ID, "rect-droppable2")
    action.drag_and_drop(drag_smile, dropbox).perform()
    assert driver.find_element(By.ID, "rect-droppable2").text == "Dropped!"

