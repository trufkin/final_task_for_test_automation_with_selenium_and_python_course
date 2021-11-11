from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def test_there_should_be_empty_basket_page(self):
        self.there_should_be_empty_basket_message()
        self.there_should_be_basket_page_title()

    def there_should_be_not_empty_basket_page(self):
        self.there_should_be_no_empty_basket_message()
        self.there_should_be_your_basket_total_table_row()

    def there_should_be_empty_basket_message(self):
        assert "Your basket is empty. Continue shopping" in \
               self.get_element_text(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Message about empty basket is either is not present on the page or is incorrect"

    def there_should_be_no_empty_basket_message(self):
        assert "Your basket is empty. Continue shopping" not in \
               self.get_element_text(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Message about empty basket is unexpectedly present on the page"

    def there_should_be_your_basket_total_table_row (self):
        assert "Basket total" in self.get_element_text(*BasketPageLocators.BASKET_TOTAL_TABLE_ROW), \
            "'Basket total' row is missing"

    def there_should_be_basket_page_title(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_PAGE_TITLE)

    def there_should_be_basket_page_with_product(self):
        self.there_should_be_no_empty_basket_message()
        self.there_should_be_basket_page_title()
