from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@when('Click settings button')
def click_settings_button(context):
    context.app.main_page.click_settings_button()


@when('Click edit profile')
def click_edit_profile(context):
    context.app.main_page.click_edit_profile()