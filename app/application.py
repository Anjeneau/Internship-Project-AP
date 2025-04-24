from pages.signin_page import SignInPage
from pages.base_page import Page
from pages.main_page import MainPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.signin_page = SignInPage(driver)
        self.main_page = MainPage(driver)
