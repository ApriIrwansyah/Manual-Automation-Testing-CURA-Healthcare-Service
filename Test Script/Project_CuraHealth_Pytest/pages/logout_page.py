from selenium.webdriver.common.by import By
from time import sleep

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_button = (By.ID, "menu-toggle")
        self.logout_link = (By.LINK_TEXT, "Logout")
        self.succes_logout = (By.XPATH, "//h1[normalize-space()='CURA Healthcare Service']")
    
    
    def logout(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.logout_link).click()
        
    def is_logout_present(self):
        return self.driver.find_element(*self.succes_logout).is_displayed()
