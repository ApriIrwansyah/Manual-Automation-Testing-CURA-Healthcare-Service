import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def driver():
    # service = Service("path_to_chromedriver")
    driver = webdriver.Chrome()
    # https://katalon-demo-cura.herokuapp.com/
    driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
    driver.maximize_window()
    yield driver
    driver.quit()
