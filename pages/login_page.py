from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
import time

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

    def register_new_user(self, email_address,  password):
        self.go_to_login_page()
        email_address_input_field = self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_ADDRESS)
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_ADDRESS).send_keys(email_address)
        password_input_field = self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        confirm_password_input_field = self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        register_button = self.is_element_present(*LoginPageLocators.REGISTER_BUTTON)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def there_should_be_registration_success_message(self):
        assert self.is_element_present(*MainPageLocators.REGISTRATION_SUCCESS_MESSAGE_ELEMENT), \
            "Registration success message is missing"

    def there_should_be_correct_registration_success_message_text(self):
        assert "Thanks for registering!" in \
               self.browser.find_element(*MainPageLocators.REGISTRATION_SUCCESS_MESSAGE).text, \
            "Registration success message text is incorrect"


