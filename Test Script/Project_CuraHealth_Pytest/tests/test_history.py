import sys
import os

from selenium.webdriver.chrome.webdriver import WebDriver
# . ini untuk keluar folder, . untuk masuk ke folder, /
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from pages.login_page import LoginPage
from pages.history_page import HistoryPage

# pytest -v tests/test_history.py

def test_view_history_success(driver: WebDriver):
    login = LoginPage(driver)
    login.login(username="John Doe", password="ThisIsNotAPassword")

    history = HistoryPage(driver)
    history.view_history()
    assert history.is_history_present()

# def test_view_history_failure_without_login(driver):
#     login = LoginPage(driver)
#     login.login(username="", password="")
    
#     history = HistoryPage(driver)
#     history.view_history()
    # assert "Please login" in driver.page_source
