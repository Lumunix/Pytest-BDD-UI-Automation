from selenium.webdriver.common.by import By
from pytest_bdd_ui_automation.pages.base import BasePage


class HomePage(BasePage):

    @property
    def PAGE_TITLE(self):
        return (By.TAG_NAME, 'h1')
    SUBHEADER = (By.TAG_NAME, 'h2')
    SUBPAGE_LINKS = (By.XPATH, '//*[@id="content"]/ul/li/a')

    def __init__(self, browser):
        self.browser = browser

    def click_page_link(self, page_name):
        links = self.browser.find_elements(*self.SUBPAGE_LINKS)
        for link in links:
            if link.text.startswith(page_name):
                link.click()
                break

    def get_page_title_text(self):
        return self.browser.find_element(*self.PAGE_TITLE).text

    def get_subheader_text(self):
        return self.browser.find_element(*self.SUBHEADER).text

    def get_subpage_list(self):
        links = self.browser.find_elements(*self.SUBPAGE_LINKS)
        titles = [link.text.split(" (")[0] for link in links]
        return titles

    def get_current_url(self):
        return self.browser.current_url
