from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import pages

class Test():
    def __init__(self):
        self.path = ChromeDriverManager().install()
        self.service = Service(executable_path=self.path)
        self.driver = None
        self.login_page = None
        self.home_page = None

    def start_session(self):
        self.driver = webdriver.Chrome(service=self.service)
        self.login_page = pages.LoginPage(driver=self.driver)
        self.home_page = pages.HomePage(driver=self.driver)

    def run_standard_login(self):
        self.start_session()
        self.driver.implicitly_wait(5)
        self.login_page.load_page()
        self.driver.implicitly_wait(5)
        self.login_page.fill_standard_login()
        self.driver.implicitly_wait(5)
        self.login_page.click_login_button()
        self.driver.implicitly_wait(5)
        self.home_page.confirm_logo_presence()
        self.driver.quit()

    def run_blocked_login(self):
        self.start_session()
        self.driver.implicitly_wait(5)
        self.login_page.load_page()
        self.driver.implicitly_wait(5)
        self.login_page.fill_failed_login()
        self.driver.implicitly_wait(5)
        self.login_page.click_login_button()
        self.driver.implicitly_wait(5)
        self.login_page.read_error()
        self.driver.quit()

if __name__ == "__main__":
    test = Test()
    test.start_session()
    test.run_standard_login()
    test.run_blocked_login()
