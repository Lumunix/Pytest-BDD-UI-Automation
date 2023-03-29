import logging
import os
import pytest
import allure
import json
from datetime import datetime
from selenium.webdriver import Remote
from WebDriverFactory import WebDriverFactory
from pytest_bdd import given, then, parsers
from allure_commons.types import AttachmentType
from pytest_bdd_ui_automation.pages.base import BasePage

DEFAULT_CONFIG_PATH = 'config.json'

def pytest_addoption(parser):
    """ Parse pytest --option variables from shell """
    parser.addoption('--config', help='Path to the configuration file to use',
                     default=DEFAULT_CONFIG_PATH)


@pytest.fixture
def config_arg(request):
    """ :returns Config path from --config option """
    return request.config.getoption('--config')


@pytest.fixture
def config(config_arg):
    browsers = ['chrome', 'firefox']

    # Read config file
    logging.info(f'Config File: {config_arg}')

    with open(os.path.join(os.path.dirname(__file__),
                           config_arg)) as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert isinstance(config['selenium_hub_url'], str)
    assert config['selenium_hub_url']
    assert config['browser'] in browsers
    assert isinstance(config['headless'], bool)
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config) -> Remote:
    """ Select configuration depends on browser and host """
    # Configure browser and driver
    driver = WebDriverFactory().get_driver(config)

    # Make call wait up to 10 seconds for elements to appear
    driver.implicitly_wait(config['implicit_wait'])

    logging.info(f"BROWSER RESOLUTION: {str(driver.get_window_size())}")
    yield driver
    driver.quit()

@pytest.fixture
def datatable():
    return DataTable()


class DataTable(object):

    def __init__(self):
        pass

    def __str__(self):
        dt_str = ''
        for field, value in self.__dict__.items():
            dt_str = f'{dt_str}\n{field} = {value}'
        return dt_str

    def __repr__(self) -> str:
        return self.__str__()


@given(parsers.parse('I have navigated to the \'the-internet\' "{page_name}" page'), target_fixture='navigate_to')
def navigate_to(browser, page_name):
    url = BasePage.PAGE_URLS.get(page_name.lower())
    browser.get(url)


@then(parsers.parse('a "{text}" banner is displayed in the top-right corner of the page'))
def verify_banner_text(browser, text):
    url = 'https://github.com/tourdedave/the-internet'
    assert text == BasePage(browser).get_github_fork_banner_text()
    assert url == BasePage(browser).get_github_fork_banner_link()
    styleAttrs = BasePage(browser).get_github_fork_banner_position().split(";")
    for attr in styleAttrs:
        if attr.startswith("position"):
            assert "absolute" == attr.split(": ")[1]
        if attr.startswith("top"):
            assert "0px" == attr.split(": ")[1]
        if attr.startswith("right"):
            assert "0px" == attr.split(": ")[1]
        if attr.startswith("border"):
            assert "0px" == attr.split(": ")[1]


@then(parsers.parse('the page has a footer containing "{text}"'))
def verify_footer_text(browser, text):
    assert text == BasePage(browser).get_page_footer_text()


@then(parsers.parse('the link in the page footer goes to "{url}"'))
def verify_footer_link_url(browser, url):
    assert url == BasePage(browser).get_page_footer_link_url()


@pytest.hookimpl(hookwrapper=True)
def pytest_allure_image_attach(item):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        feature_request = item.funcargs['request']
        driver = feature_request.getfixturevalue('browser')
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            timestamp = datetime.now().strftime('%m-%d-%Y:%H-%M-%S')
            screenshot_path = report.head_line + ':' + timestamp + '.png'
            driver.save_screenshot(screenshot_path)
            allure.attach(driver.get_screenshot_as_png(), name=screenshot_path, attachment_type=AttachmentType.PNG)

