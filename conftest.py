import logging
import os
import pytest
import json
from datetime import datetime
from selenium.webdriver import Remote
from DriverFactory import DriverFactory


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
def url():
    namespace = os.environ.get('NAMESPACE')
    kubernetes_cluster = os.environ.get('KUBERNETES_CLUSTER')
    if not namespace:
        raise Exception(f'NAMESPACE environment variable not set, '
                        f'set using export NAMESPACE=YOUR_NAMESPACE or in ~/bash_profile.')
    if not kubernetes_cluster:
        raise Exception(f'KUBERNETES_CLUSTER environment variable not set, '
                        f'set using export KUBERNETES_CLUSTER=CLUSTER_NAME or in ~/bash_profile.')

    return f'http://{namespace}.{kubernetes_cluster}.do-alert-innovation.com/{namespace}/acs/console'


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
def browser(config, url) -> Remote:
    """ Select configuration depends on browser and host """
    # Configure browser and driver
    driver = DriverFactory().get_driver(config)

    # Make call wait up to 10 seconds for elements to appear
    driver.implicitly_wait(config['implicit_wait'])

    logging.info(f"BROWSER RESOLUTION: {str(driver.get_window_size())}")
    logging.info(f'URL: {url}')

    yield driver
    driver.quit()


@pytest.fixture
def pages(url):
    return {
        "login": f'{url}' + "/login",
        "bots": f'{url}' + "/home/system/bots",
        "totes": f'{url}' + "/home/system/totes",
        "workstations": f'{url}' + "/home/system/workstations",
        "safety": f'{url}' + "/home/system/safety",
        "activity": f'{url}' + "/home/system/activity",
        "user areas": f'{url}' + "/home/system/userAreas",
        "configs": f'{url}' + "/home/system/configs",
        "user actions": f'{url}' + "/home/userActions",
        "bot cycles": f'{url}' + "/home/testing/botCycles"
    }

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        feature_request = item.funcargs['request']
        driver = feature_request.getfixturevalue('browser')
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            timestamp = datetime.now().strftime('%m-%d-%Y:%H-%M-%S')
            screenshot_path = report.head_line + ':' + timestamp + '.png'
            driver.save_screenshot(screenshot_path)
            extra.append(pytest_html.extras.url(driver.current_url))
            extra.append(pytest_html.extras.image(screenshot_path))
        report.extra = extra
