from selenium.webdriver.common.by import By

class HistoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_toggle    = (By.ID, "menu-toggle")
        self.history_link = (By.LINK_TEXT, "History")
        self.history_table = (By.XPATH, "//h2[normalize-space()='History']")
    
    def view_history(self):
        self.driver.find_element(*self.menu_toggle).click()
        self.driver.find_element(*self.history_link).click()
    
    def is_history_present(self):
        return self.driver.find_element(*self.history_table).is_displayed()
