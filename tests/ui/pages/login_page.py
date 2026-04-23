from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    URL = "https://automationexercise.com/login"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
            self.driver.get(self.URL)

    def enter_email(self, email):
            field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='login-email']")))
            field.clear()
            field.send_keys(email)

    def enter_password(self, password):
            field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='login-password']")))
            field.clear()
            field.send_keys(password)

    def click_login(self):
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='login-button']"))).click()

    def get_error_message(self):
            error = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p[style*='color: red']")))
            return error.text        

    


