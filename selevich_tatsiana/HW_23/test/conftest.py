import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selevich_tatsiana.HW_23.pages.item_page import ItemPage
from selevich_tatsiana.HW_23.pages.main_page import MainPage
from selevich_tatsiana.HW_23.pages.cart_page import CartPage


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.onliner.by/")
    return driver


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


@pytest.fixture(autouse=True)
def item_page(driver):
    yield ItemPage(driver)


@pytest.fixture(autouse=True)
def cart_page(driver):
    yield CartPage(driver)
