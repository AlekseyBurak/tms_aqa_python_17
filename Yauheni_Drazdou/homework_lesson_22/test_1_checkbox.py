from selenium.webdriver.common.by import By

def test_checkbox(driver):
    #go to checkbox
    driver.get("https://www.qa-practice.com/elements/checkbox/single_checkbox")
    #Single_checkbox btn
    driver.find_element(By.XPATH, "//*[@href='/elements/checkbox/single_checkbox']").click()
    #select_me_or_not
    driver.find_element(By.ID, "submit-id-submit").click() #checkbox was not selected, the result is not displayed
    driver.find_element(By.ID, "id_checkbox_0").click() #checkbox has been selected
    driver.find_element(By.ID, "submit-id-submit").click()
    #the name of the selected checkbox is displayed to the user
    assert driver.find_element(By.ID, "result-text").text == "select me or not"
    #Checkboxes
    driver.find_element(By.XPATH, "//*[@href='/elements/checkbox/mult_checkbox']").click()
    driver.find_element(By.ID, "submit-id-submit").click() #no checkbox was selected, the result is not displayed

    #Testing different checkboxes
    driver.find_element(By.ID, "id_checkboxes_0").click() #select "one"
    driver.find_element(By.ID, "submit-id-submit").click()
    #the name of "one" is displayed
    assert driver.find_element(By.ID, "result-text").text == "one"

    driver.find_element(By.ID, "id_checkboxes_1").click() #select "two"
    driver.find_element(By.ID, "submit-id-submit").click()
    #the name of "two" is displayed
    assert driver.find_element(By.ID, "result-text").text == "two"

    driver.find_element(By.ID, "id_checkboxes_2").click()  #select "three"
    driver.find_element(By.ID, "submit-id-submit").click()
    #the name of "three" is displayed
    assert driver.find_element(By.ID, "result-text").text == "three"

    #select "one" "two" "three"
    driver.find_element(By.ID, "id_checkboxes_0").click()
    driver.find_element(By.ID, "id_checkboxes_1").click()
    driver.find_element(By.ID, "id_checkboxes_2").click()
    driver.find_element(By.ID, "submit-id-submit").click()
    #the names of "one-two-three" are displayed
    assert driver.find_element(By.ID, "result-text").text == "one, two, three"

