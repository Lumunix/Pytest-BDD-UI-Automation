from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class WebDriverFactory:
    def get_driver(self, config) -> WebDriver:

        if config['browser'] == 'firefox':
            firefox_options = webdriver.FirefoxOptions()
            driver = webdriver.Remote(
                options=self.set_driver_options(config, firefox_options),
                command_executor=config['selenium_hub_url'])
        elif config['browser'] == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            driver = webdriver.Remote(
                options=self.set_driver_options(config, chrome_options),
                command_executor=config['selenium_hub_url'])
        else:
            raise Exception(f'Browser "{config["browser"]}" is not supported')

        return driver

    @staticmethod
    def set_driver_options(config, options):
        options.add_argument('start-maximized')
        options.add_argument('window-size=1920x1080')
        options.set_capability("se:recordVideo", "true")
        options.set_capability("se:screenResolution", "1920x1080")
        if config['headless']:
            options.add_argument('headless')

        return options
