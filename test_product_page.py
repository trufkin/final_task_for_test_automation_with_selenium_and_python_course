import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time


@pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, url):
    page = ProductPage(browser, url)
    page.open(browser, url)
    page.there_should_be_product_page()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.basket_price_should_equal_product_price()
    page.product_name_in_success_message_is_correct()


@pytest.mark.parametrize('url', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207",marks=pytest.mark.xfail)])
@pytest.mark.negativechecks
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, url):
    page = ProductPage(browser, url)
    page.open(browser, url)
    page.add_product_to_basket()
    page.should_not_be_success_message()



@pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
@pytest.mark.negativechecks
def test_guest_cant_see_success_message(browser, url):
    page = ProductPage(browser, url)
    page.open(browser, url)
    page.should_not_be_success_message()

@pytest.mark.parametrize('url', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207",marks=pytest.mark.xfail)])
@pytest.mark.negativechecks
def test_message_disappeared_after_adding_product_to_basket(browser, url):
    page = ProductPage(browser, url)
    page.open(browser, url)
    page.add_product_to_basket()
    page.should_disappear_element_specified()

@pytest.mark.inheritancepluses
def test_guest_should_see_login_link_on_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open(browser, url)
    page.there_should_be_login_link()

@pytest.mark.inheritancepluses
def test_guest_can_go_to_login_page_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open(browser, url)
    page.go_to_login_page()
    page.there_should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, url)
    product_page.open(browser, url)
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.test_there_should_be_empty_basket_page()

@pytest.mark.newcase
def test_guest_can_see_product_in_basket_opened_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    product_page = ProductPage(browser, url)
    product_page.open(browser, url)
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.there_should_be_not_empty_basket_page()
