from selenium.webdriver.common.by import By
from pytest_bdd_ui_automation.pages.base import BasePage

class FormAuthenticationPage(BasePage):

    @property
    def PAGE_TITLE(self):
        return (By.TAG_NAME, 'h2')
    OPENING_PARAGRAPH = (By.CLASS_NAME, 'subheader')
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    INPUT_LABEL = (By.XPATH, './../label')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    MESSAGE_BANNER = (By.ID, 'flash')
    LOGOUT_BUTTON = (By.CLASS_NAME, 'button')

    def __init__(self, browser):
        self.browser = browser

    def get_page_title_text(self):
        return self.browser.find_element(*self.PAGE_TITLE).text

    def get_opening_paragraph_text(self):
        return self.browser.find_element(*self.OPENING_PARAGRAPH).text

    def is_username_input_displayed(self):
        return self.browser.find_element(*self.USERNAME).is_displayed()

    def get_username_input_label_text(self):
        return self.browser.find_element(*self.USERNAME).find_element(*self.INPUT_LABEL).text
    
    def is_password_input_displayed(self):
        return self.browser.find_element(*self.PASSWORD).is_displayed()

    def get_password_input_label_text(self):
        return self.browser.find_element(*self.PASSWORD).find_element(*self.INPUT_LABEL).text 

    def is_login_button_displayed(self):
        return self.browser.find_element(*self.LOGIN_BUTTON).is_displayed()

    def get_login_button_text(self):
        return self.browser.find_element(*self.LOGIN_BUTTON).text

    def click_login_button(self):
        return self.browser.find_element(*self.LOGIN_BUTTON).click()

    def is_message_banner_displayed(self):
        return self.browser.find_element(*self.MESSAGE_BANNER).is_displayed()

    def get_message_banner_colour(self):
        return self.browser.find_element(*self.MESSAGE_BANNER).value_of_css_property('background-color')

    def get_message_banner_text(self):
        # Full text includes 'x' to close the message so need to strip this off
        return self.browser.find_element(*self.MESSAGE_BANNER).text.split('\n')[0]

    def enter_username(self, username):
        self.browser.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.browser.find_element(*self.PASSWORD).send_keys(password)

    def is_logout_button_displayed(self):
        return self.browser.find_element(*self.LOGOUT_BUTTON).is_displayed()

    def get_logout_button_text(self):
        return self.browser.find_element(*self.LOGOUT_BUTTON).text 
    
    def get_current_url(self):
        return self.browser.current_url