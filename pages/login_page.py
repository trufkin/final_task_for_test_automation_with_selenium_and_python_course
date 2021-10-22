from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def there_should_be_login_page(self):
        self.there_should_be_login_url()
        self.there_should_be_login_form()
        self.there_should_be_register_form()

    def there_should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, "It looks like current page does not contain 'login' word in the URL"

    def there_should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def there_should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not present"

