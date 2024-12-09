import sys
import os
# pytest tests/test_login.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from pages.login_page import LoginPage

def test_login_success(driver):
    login = LoginPage(driver)
    login.login(username="John Doe", password="ThisIsNotAPassword")
    assert "Make Appointment" in login.get_success_messasge()  # Sukses masuk ke halaman appointment 
# ?
def test_login_failure(driver):
    login = LoginPage(driver)
    login.login(username="InvalidUser", password="WrongPassword")
    assert "Login failed! Please ensure the username and password are valid." in login.get_error_message()
