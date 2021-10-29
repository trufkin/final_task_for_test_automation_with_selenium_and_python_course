from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form.well")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form.well")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_DESCRIPTION_SECTION = (By.CSS_SELECTOR, "#product_description")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_MAIN_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "header .page_inner a[href$=\"/basket/\"].btn.btn-default")
    BASKET_MINI_PRICE = (By.CSS_SELECTOR, "div.basket-mini")
    ADDED_TO_BASKET_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner strong")

