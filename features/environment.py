from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from support.logger import logger
from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
  ## CHROME ##
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

 ## HEADLESS MODE ##
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

 ## FIREFOX ##
    # driver_path = GeckoDriverManager().install()
    # service = FirefoxService(driver_path)
    # context.driver = webdriver.Firefox(service=service)

 ## BROWSERSTACK ##
    bs_user = 'anjeneauprivott_lPAHbU'
    bs_key = 'Bj1xdbGtSNZkoe3ozHsn'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        "deviceName": "iPhone XR",
        "osVersion": "15",
        'browserName': 'chromium',
        'sessionName': scenario_name,
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)





    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


# def before_scenario(context, scenario):
#     print('\nStarted scenario: ', scenario.name)
#     browser_init(context, scenario.name)

def before_scenario(context, scenario):
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


# def before_step(context, step):
#     print('\nStarted step: ', step)

def before_step(context, step):
    logger.info(f'Started step: {step}')


# def after_step(context, step):
#     if step.status == 'failed':
#         print('\nStep failed: ', step)

def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.quit()

# Command to run tests with Allure & Behave:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features
# allure serve test_results/