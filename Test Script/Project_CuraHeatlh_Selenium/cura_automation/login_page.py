from selenium.webdriver.common.by import By
from time import sleep
# from base import BasePage

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # https://katalon-demo-cura.herokuapp.com/profile.php#login
        self.login_button   = (By.ID, "btn-make-appointment")
        # https://katalon-demo-cura.herokuapp.com/profile.php#login
        self.menu_toggle    = (By.ID, "menu-toggle")
        self.link_text      = (By.LINK_TEXT, "Login")
        self.username_field = (By.ID, "txt-username")
        self.password_field = (By.ID, "txt-password")
        self.submit_button  = (By.ID, "btn-login")

    def login(self, username, password):
        self.driver.find_element(By.ID, "btn-make-appointment").click()
        sleep(2)
        self.driver.find_element(By.ID, "txt-username").send_keys(username)
        sleep(2)
        self.driver.find_element(By.ID, "txt-password").send_keys(password)
        sleep(2)
        self.driver.find_element(By.ID, "btn-login").click()
        print("Berhasil Masuk ke halaman : " + self.driver.title)
        
    # def login_invalid(self):
    #     self.driver.find_element(By.ID, "menu-toggle").click()
    #     self.driver.find_element(By.LINK_TEXT, "Login").click()
    #     sleep(2)
