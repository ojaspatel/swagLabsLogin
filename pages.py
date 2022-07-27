from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username_field = None
        self.password_field = None
        self.login_button = None
        self.error = None
        self.standard_user = "standard_user"
        self.locked_out_user = "locked_out_user"
        self.password = "secret_sauce"

    def load_page(self):
        self.driver.get("https://www.saucedemo.com")

    def define_fields(self):
        self.username_field = self.driver.find_element(By.NAME, "user-name")
        self.password_field = self.driver.find_element(By.NAME, "password")
        self.login_button = self.driver.find_element(By.NAME, "login-button")
        self.error = self.driver.find_element(By.CLASS_NAME,
                                              "error-message-container")

    def fill_standard_login(self):
        self.define_fields()
        self.driver.implicitly_wait(5)
        self.username_field.send_keys(self.standard_user)
        self.driver.implicitly_wait(5)
        self.password_field.send_keys(self.password)
        self.driver.implicitly_wait(5)

    def fill_failed_login(self):
        self.define_fields()
        self.driver.implicitly_wait(5)
        self.username_field.send_keys(self.locked_out_user)
        self.driver.implicitly_wait(5)
        self.password_field.send_keys(self.password)
        self.driver.implicitly_wait(5)

    def click_login_button(self):
        self.define_fields()
        self.login_button.click()


    def read_error(self):
        self.define_fields()
        if "Epic sadface" in self.error.text:
            print("User lockout successful.")
        else:
            print("Login successful. User lockout failed.")
        return self.error.text


class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.logo = None

    def load_page(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")

    def confirm_logo_presence(self):
        self.logo = self.driver.find_element(By.CLASS_NAME, "app_logo")
        if self.logo:
            print("App logo exists. Successful login confirmed.")
            return True
        else:
            print("App logo not found. Login failed.")
            return False
