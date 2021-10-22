from .pages.main_page import MainPage
import time

def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url)
    page.open(browser, url)
    time.sleep(5)
    page.go_to_login_page()
    time.sleep(5)

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open(browser, link)
    page.there_should_be_login_link()


