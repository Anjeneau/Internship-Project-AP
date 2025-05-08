from selenium.webdriver.common.by import By
from pages.base_page import Page
from webdriver_manager.firefox import GeckoDriverManager

class SignInPage(Page):
    ENTER_NAME = (By.CSS_SELECTOR, "[wized='nameInputProfile']")
    ENTER_PASSWORD = (By.ID, 'field')
    ENTER_PHONE = (By.ID, 'phone2')
    ENTER_EMAIL = (By.ID, 'email-2')
    SIGNIN_BTN = (By.CSS_SELECTOR, "[wized='loginButton']")
    SAVE_BTN = (By.CSS_SELECTOR, "[wized='saveButtonProfile']")
    CLOSE_BTN = (By.XPATH, "//a[text()='Close']")


    def enter_name(self, info):
        self.input_text(info, *self.ENTER_NAME)

    def enter_phone(self, info):
        self.input_text(info, *self.ENTER_PHONE)

    def enter_email(self, info):
        self.input_text(info, *self.ENTER_EMAIL)

    def enter_pw(self, info):
        self.input_text(info, *self.ENTER_PASSWORD)

    def click_signin_button(self):
        self.click(*self.SIGNIN_BTN)

    def click_save_button(self):
        self.click(*self.SAVE_BTN)

    def click_close_button(self):
        self.click(*self.CLOSE_BTN)

    def verify_information_present(self):
        #self.verify_text('Jane Day', (By.ID, 'Full-Name'))
        self.get_text(By.ID, 'Full-Name')