from cura_automation.base import BasePage
from cura_automation.login_page import LoginPage
from cura_automation.appointment_page import MakeAppointment
from cura_automation.history_page import HistoryPage
from cura_automation.logout_page import LogoutPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from login_page import LoginPage
# from appointment_page import AppointmentPage
# from history_page import HistoryPage
# from logout_page import LogoutPage
import time

if __name__ == "__main__":
    # Inisialisasi Browser
    base = BasePage()
    driver = base.driver
    
    try:
        # Login
        login_page = LoginPage(driver)
        login_page.login("John Doe", "ThisIsNotAPassword")
        
        # Book Appointment
        appointment_page = MakeAppointment(driver)
        appointment_page.book_appointment(facility="Tokyo CURA Healthcare Center", date="12/15/2024", comment="Routine checkup")
        
        
        # View history
        history = HistoryPage(driver)
        history.view_history()
        time.sleep(3)  # Tunggu sebentar untuk melihat history

        # Logout
        # logout = LogoutPage(driver)
        # logout.logout()

    
    finally:
        # Close the browser
        base.quit()
