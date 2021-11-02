import pytest
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
import time


def test_guest_should_see_login_link(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, url)
    main_page.open(browser, url)
    main_page.there_should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url)
    page.open(browser, url)
    time.sleep(5)
    page.go_to_login_page()
    time.sleep(5)


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, url)
    main_page.open(browser, url)
    main_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.test_there_should_be_empty_basket_page()


@pytest.mark.newcase
def test_guest_can_see_product_in_basket_opened_from_main_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, url)
    main_page.open(browser, url)
    main_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.there_should_be_not_empty_basket_page()
