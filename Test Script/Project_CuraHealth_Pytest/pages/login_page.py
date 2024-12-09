from selenium.webdriver.common.by import By
from time import sleep

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_button       = (By.ID, "btn-make-appointment")
        self.username_field     = (By.ID, "txt-username")
        self.password_field     = (By.ID, "txt-password")
        self.submit_button      = (By.ID, "btn-login")
        self.error_message      = (By.XPATH, "//p[@class='lead text-danger']")
        self.success_login      = (By.XPATH, "//h2[normalize-space()='Make Appointment']")

    def login(self, username, password):
        self.driver.find_element(*self.login_button).click()
        sleep(2)
        self.driver.find_element(*self.username_field).send_keys(username)
        sleep(2)
        self.driver.find_element(*self.password_field).send_keys(password)
        sleep(2)
        self.driver.find_element(*self.submit_button).click()
        sleep(2)
        # return self.driver.find_element(*self.success_login).text

    def get_success_messasge(self):
        return self.driver.find_element(*self.success_login).text
    
    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
