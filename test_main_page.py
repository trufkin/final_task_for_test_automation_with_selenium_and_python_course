from .pages.main_page import MainPage
import time

def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url)
    page.open(browser, url)
    time.sleep(5)
    page.go_to_login_page()
    time.sleep(5)

