from pages.base_page import Page
from pages.signin_page import SignInPage
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep



class MainPage(Page):
    SETTINGS_BTN = (By.CSS_SELECTOR, "[class='g-menu-text']")
    EDIT_BTN = (By.XPATH, "//div[text()='Edit profile']")

    def click_settings_button(self):
        self.click(*self.SETTINGS_BTN)


    def click_edit_profile(self):
        self.click(*self.EDIT_BTN)