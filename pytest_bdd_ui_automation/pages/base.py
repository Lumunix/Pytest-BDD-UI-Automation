from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By

class BasePage():

    BASE_URL = "https://the-internet.herokuapp.com"

    PAGE_URLS = {
        "home": BASE_URL + "/",
        "checkboxes": BASE_URL + "/checkboxes",
        "dropdown": BASE_URL + "/dropdown",
        "dynamic controls": BASE_URL + "/dynamic_controls",
        "form authentication": BASE_URL + "/login",
        "inputs": BASE_URL + "/inputs",
        "secure area": BASE_URL + "/secure"
    }

    @property
    @abstractmethod
    def PAGE_TITLE(self):
      pass

    @abstractmethod
    def get_page_title_text(self):
      pass

    FORK_LINK = (By.XPATH, "/html/body/div[2]/a")
    FORK_LINK_IMG = (By.XPATH, "/html/body/div[2]/a/img")
    FOOTER = (By.ID, "page-footer")
    FOOTER_LINK = (By.XPATH, "//*[@id=\"page-footer\"]//a")

    def __init__(self, browser):
        self.browser = browser

    def get_github_fork_banner_text(self):
      return self.browser.find_element(*self.FORK_LINK_IMG).get_attribute("alt")

    def get_github_fork_banner_link(self):
      return self.browser.find_element(*self.FORK_LINK).get_attribute("href")

    def get_github_fork_banner_position(self):
      return self.browser.find_element(*self.FORK_LINK_IMG).get_attribute("style")

    def get_page_footer_text(self):
      return self.browser.find_element(*self.FOOTER).text

    def get_page_footer_link_url(self):
      return self.browser.find_element(*self.FOOTER_LINK).get_attribute("href")