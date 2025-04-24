from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@given('Open signin page')
def open_signin_page(context):
    context.driver.get('https://soft.reelly.io')


@when('Click signin button')
def click_signin_button(context):
    context.app.signin_page.click_signin_button()


@when('Enter name in input field {info}')
def enter_name(context, info):
    context.app.signin_page.enter_name(info)


@when('Enter phone in input field {info}')
def enter_phone(context, info):
    context.app.signin_page.enter_phone(info)


@when('Enter email {info}')
def enter_email(context, info):
    context.app.signin_page.enter_email(info)


@when('Enter password in input field {info}')
def enter_pw(context, info):
    context.app.signin_page.enter_pw(info)


@when('Click save button')
def click_save_button(context):
    context.app.signin_page.click_save_button()
    sleep(5)


@then('Click close button')
def click_close_button(context):
    context.app.signin_page.click_close_button()
    sleep(5)


@then('Verify correct information is present')
def verify_information_present(context):
    context.app.signin_page.verify_information_present()