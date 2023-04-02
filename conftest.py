import logging
import os
import pytest
import allure
import json
from datetime import datetime
from selenium.webdriver import Remote
from WebDriverFactory import WebDriverFactory
from allure_commons.types import AttachmentType


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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        feature_request = item.funcargs['request']
        driver = feature_request.getfixturevalue('browser')
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            timestamp = datetime.now().strftime('%m-%d-%Y:%H-%M-%S')
            screenshot = report.head_line + ':' + timestamp + '.png'
            allure.attach(driver.get_screenshot_as_png(), name=screenshot, attachment_type=AttachmentType.PNG)

