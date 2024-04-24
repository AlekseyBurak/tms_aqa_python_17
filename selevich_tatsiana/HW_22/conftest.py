import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    return driver


@pytest.fixture()
def driver(request):
    driver = create_driver()
    marker = request.node.get_closest_marker('url')

    if marker is None:
        pytest.skip('Url is not provided')

    url = marker.args[0]
    driver.get(url)

    return driver
