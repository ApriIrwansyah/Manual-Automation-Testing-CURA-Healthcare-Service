from selenium.webdriver.common.by import By

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_button = (By.XPATH, "//a[@id='menu-toggle']")
        self.logout_link = (By.LINK_TEXT, "Logout")
    
    def logout(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.logout_link).click()
