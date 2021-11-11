from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def there_should_be_product_page(self):
        self.there_should_be_add_to_basket_button()
        self.there_should_be_product_description()
        self.there_should_be_main_price()

    def there_should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is missing"

    def there_should_be_product_description(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_DESCRIPTION_SECTION), "Description section is missing"

    def there_should_be_main_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_MAIN_PRICE), "Product main price label is missing"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_SUCCESS_MESSAGE), \
            "Success message is present, but should not be"

    def should_disappear_element_specified(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_BASKET_SUCCESS_MESSAGE), \
            "Success message is present, but should not be"

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def basket_price_should_equal_product_price(self):
        product_main_price = self.browser.find_element(*ProductPageLocators.PRODUCT_MAIN_PRICE).text.strip()
        basket_mini_price = self.browser.find_element(*ProductPageLocators.BASKET_MINI_PRICE).text.strip()
        assert product_main_price in basket_mini_price, "Product price and basket total value are not the same"

    def product_name_in_success_message_is_correct(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text.strip()
        add_to_basket_success_message = self.browser.find_element(
            *ProductPageLocators.ADDED_TO_BASKET_SUCCESS_MESSAGE).text.strip()
        assert product_name == add_to_basket_success_message, \
            "Product name specified in the success message and name of added product are not the same "
