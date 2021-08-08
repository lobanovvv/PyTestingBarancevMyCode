import pytest
from selenium import webdriver


@pytest.fixture()
def wd():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1400,800")
    # Suppress bluetooth chrome error
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    wd = webdriver.Chrome(options=chrome_options)
    wd.get("http://localhost/addressbook")
    return wd
