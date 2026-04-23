from tests.ui.pages.login_page import LoginPage

class TestLogin:

    def test_login_with_invalid_credentials(self, driver):
        page = LoginPage(driver)
        page.open()
        page.enter_email("invalid@test.com")
        page.enter_password("wrongpassword")
        page.click_login()
        error = page.get_error_message()
        assert "Your email or password is incorrect" in error


    def test_login_with_empty_credentials (self, driver):
        page = LoginPage(driver)
        page.open()
        page.click_login()
        assert "login" in driver.current_url