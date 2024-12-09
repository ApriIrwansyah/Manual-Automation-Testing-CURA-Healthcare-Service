from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

class AppointmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.facility_dropdown = (By.ID, "combo_facility")
        self.apply_checkbox = (By.ID, "chk_hospotal_readmission")
        self.medicaid_radio = (By.ID, "radio_program_medicaid")
        self.visit_date = (By.ID, "txt_visit_date")
        self.comment_box = (By.ID, "txt_comment")
        self.book_button = (By.ID, "btn-book-appointment")
        self.confirmation_message = (By.CLASS_NAME, "text-center")
    
    def book_appointment(self, facility, date, comment):
        Select(self.driver.find_element(*self.facility_dropdown)).select_by_visible_text(facility)
        sleep(1)
        self.driver.find_element(*self.apply_checkbox).click()
        sleep(1)
        self.driver.find_element(*self.medicaid_radio).click()
        sleep(1)
        self.driver.find_element(*self.visit_date).send_keys(date)
        sleep(1)
        self.driver.find_element(*self.comment_box).send_keys(comment)
        sleep(1)
        self.driver.find_element(*self.book_button).click()

    def get_confirmation_message(self):
        return self.driver.find_element(*self.confirmation_message).text
