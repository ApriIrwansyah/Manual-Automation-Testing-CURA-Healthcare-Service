import sys
import os

from selenium.webdriver.chrome.webdriver import WebDriver
# . ini untuk keluar folder, . untuk masuk ke folder, /
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from pages.login_page import LoginPage
from pages.appointment_page import AppointmentPage
from pages.history_page import HistoryPage

# pytest -v tests/test_appointment.py

def test_appointment_success(driver):
    login = LoginPage(driver)
    login.login(username="John Doe", password="ThisIsNotAPassword")

    appointment = AppointmentPage(driver)
    appointment.book_appointment("Tokyo CURA Healthcare Center", "12/15/2024", "Routine checkup")
    assert "Appointment Confirmation" in appointment.get_confirmation_message()

def test_appointment_failure_missing_date(driver: WebDriver):
    login = LoginPage(driver)
    login.login(username="John Doe", password="ThisIsNotAPassword")

    appointment = AppointmentPage(driver)
    appointment.book_appointment("Tokyo CURA Healthcare Center", "", "Missing date")
    # assert "Please fill out this field." in driver.page_source
