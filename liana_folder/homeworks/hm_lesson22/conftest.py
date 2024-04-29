import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from liana_folder.homeworks.hm_lesson22.locators import URL


@pytest.fixture(autouse=True)
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.get(URL)
    yield driver
