from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

class HistoryPage:
    def __init__(self, driver):
        self.driver = driver
        # Form Login
        self.login_button       = (By.ID, "btn-make-appointment")
        self.menu_toggleL        = (By.ID, "menu-toggle")
        self.link_text          = (By.LINK_TEXT, "Login")
        self.username_field     = (By.ID, "txt-username")
        self.password_field     = (By.ID, "txt-password")
        self.submit_button      = (By.ID, "btn-login")
        # Form Appointment
        self.facility_dropdown  = (By.ID, "combo_facility")
        self.apply_checkbox     = (By.XPATH, " //input[@id='chk_hospotal_readmission']")
        self.healthcare_radio   = (By.ID, "radio_program_medicaid")
        self.visit_date         = (By.ID, "txt_visit_date")
        self.comment_box        = (By.ID, "txt_comment")
        self.book_button        = (By.ID, "btn-book-appointment")
        # History   
        self.menu_toggleH        = (By.ID, "menu-toggle")
        self.history_link       = (By.LINK_TEXT, "History")
        self.Homapage           = (By.XPATH, "//a[@class='btn btn-default']")
    
    def view_history(self):
        self.driver.find_element(*self.history_link).click()
