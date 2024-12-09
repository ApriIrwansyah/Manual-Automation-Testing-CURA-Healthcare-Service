import os 
import sys

# pytest -v tests/test_logout.py


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage

def test_logout_page(driver):
    # Form Login
    login   = LoginPage(driver)
    login.login(username="John Doe", password="ThisIsNotAPassword")
    assert "Make Appointment" in login.get_success_messasge()  # Sukses masuk ke halaman appointment  
    
    # Form Logout
    logout = LogoutPage(driver)
    logout.logout()
    assert logout.is_logout_present()