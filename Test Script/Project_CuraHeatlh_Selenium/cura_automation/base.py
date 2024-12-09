from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class BasePage:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome()
        self.driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
        self.driver.maximize_window()
        sleep(2)
    
    def quit(self):
        self.driver.quit()
