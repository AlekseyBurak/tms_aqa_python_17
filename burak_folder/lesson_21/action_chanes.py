from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = Options()

url = "https://www.qa-practice.com/elements/alert/alert"


driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

action = ActionChains(driver)
action.move_to_element(menu).click(hidden_submenu).perform()

action.key_down(Keys.CONTROL).click().key_up(Keys.CONTROL).perform()
driver.get_screenshot_as_png()

# JS

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

element = driver.find_element(By.ID, "myid")
driver.execute_script("arguments[0].click();", element)