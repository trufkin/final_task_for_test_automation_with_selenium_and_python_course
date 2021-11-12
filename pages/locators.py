from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_OR_REGISTER_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_OR_REGISTER_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "a[href='/en-gb/basket/']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_OR_REGISTER_LINK = (By.CSS_SELECTOR, "#login_link")
    REGISTRATION_SUCCESS_MESSAGE_ELEMENT = (By.CSS_SELECTOR, ".alert.alert-success.fade.in")
    REGISTRATION_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner.wicon")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form.well")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form.well")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTER_EMAIL_ADDRESS = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit'].btn.btn-lg.btn-primary")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_DESCRIPTION_SECTION = (By.CSS_SELECTOR, "#product_description")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_MAIN_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "header .page_inner a[href$=\"/basket/\"].btn.btn-default")
    BASKET_MINI_PRICE = (By.CSS_SELECTOR, "div.basket-mini")
    ADDED_TO_BASKET_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner strong")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_PAGE_TITLE = (By.CSS_SELECTOR, ".page-header.action h1")
    BASKET_TOTAL_TABLE_ROW = (By.CSS_SELECTOR, "#basket_totals .total")
