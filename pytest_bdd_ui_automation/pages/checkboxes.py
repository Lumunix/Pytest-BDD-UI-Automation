from selenium.webdriver.common.by import By
from pytest_bdd_ui_automation.pages.base import BasePage


class CheckboxesPage(BasePage):

    @property
    def PAGE_TITLE(self):
        return (By.TAG_NAME, 'h3')
    CHECKBOXES_FORM = (By.ID, 'checkboxes')
    ALL_CHECKBOXES = (By.XPATH, '//*[@id="checkboxes"]/input')

    def __init__(self, browser):
        self.browser = browser

    def get_page_title_text(self):
        return self.browser.find_element(*self.PAGE_TITLE).text

    def get_num_checkboxes(self):
        return len(self.browser.find_elements(*self.ALL_CHECKBOXES))

    def get_checkbox_labels(self):
        return self.browser.find_element(*self.CHECKBOXES_FORM).text.split("\n")
    
    def get_checkbox_checked_state(self, index):
        return self.browser.find_elements(*self.ALL_CHECKBOXES)[index].get_attribute("checked") == 'true'

    def click_checkbox(self, index):
        return self.browser.find_elements(*self.ALL_CHECKBOXES)[index].click()

    
