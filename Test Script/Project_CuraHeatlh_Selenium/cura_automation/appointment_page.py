from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from time import sleep

class MakeAppointment:
    
    def __init__(self, driver):
        self.driver = driver
        self.facility_dropdown      = (By.ID, "combo_facility")
        self.apply_checkbox         = (By.XPATH, " //input[@id='chk_hospotal_readmission']")
        self.healthcare_radio       = (By.ID, "radio_program_medicaid")
        self.visit_date             = (By.ID, "txt_visit_date")
        self.comment_box            = (By.ID, "txt_comment")
        self.book_button            = (By.ID, "btn-book-appointment")
        # Form History
        self.menu_toggleH        = (By.ID, "menu-toggle")
        self.history_link       = (By.LINK_TEXT, "History")
        self.Homapage           = (By.XPATH, "//a[@class='btn btn-default']")
        
    def book_appointment(self, facility, date, comment):
        # Dropdown
        Select(self.driver.find_element(*self.facility_dropdown)).select_by_visible_text(facility)
        self.driver.find_element(*self.apply_checkbox).click()
        self.driver.find_element(*self.healthcare_radio).click()
        self.driver.find_element(*self.visit_date).send_keys(date)
        self.driver.find_element(*self.comment_box).send_keys(comment)
        self.driver.find_element(*self.book_button).click()
        print("Berhasil ditambahkan : " + self.driver.title)
        