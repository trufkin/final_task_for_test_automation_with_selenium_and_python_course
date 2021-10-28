from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_login_page_is_open(browser):
    link = "http://selenium1py.pythonanywhere.com"
    main_page = MainPage(browser, link)
    main_page.open(browser, link)
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.there_should_be_login_page()
    login_page.there_should_be_register_form()
