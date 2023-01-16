from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd_ui_automation.pages.base import BasePage


class DynamicControlsPage(BasePage):

    @property
    def PAGE_TITLE(self):
        return (By.TAG_NAME, 'h4')
    OPENING_PARAGRAPH = (By.TAG_NAME, 'p')
    SECTION_HEADER = (By.CLASS_NAME, 'subheader')
    HORIZONTAL_RULE = (By.XPATH, '//div[@class="example"]/hr')
    CHECKBOX_EXAMPLE_FORM = (By.ID, 'checkbox-example')
    INPUT_EXAMPLE_FORM = (By.ID, 'input-example')
    BUTTON = (By.TAG_NAME, 'button')
    CHECKBOX_LABEL = (By.XPATH, './*[@id="checkbox"]')
    INPUT = (By.TAG_NAME, 'input')
    PARENT = (By.XPATH, './..')
    BUTTON = (By.TAG_NAME, 'button')
    BUTTON_BY_TEXT = (By.XPATH, '//button[text()="%s"]')
    LOADING_BAR = (By.ID, 'loading')
    MESSAGE = (By.ID, 'message')
    ALTERNATIVE_CHECKBOX = (By.ID, 'checkbox')

    def __init__(self, browser):
        self.browser = browser

    def get_page_title_text(self):
        return self.browser.find_element(*self.PAGE_TITLE).text

    def get_opening_paragraph_text(self):
        return self.browser.find_element(*self.OPENING_PARAGRAPH).text

    def get_num_sections(self):
        return len(self.browser.find_elements(*self.SECTION_HEADER))

    def get_section_headers_text(self):
        return [header.text for header in self.browser.find_elements(*self.SECTION_HEADER)]

    def get_num_horizontal_rules(self):
        return len(self.browser.find_elements(*self.HORIZONTAL_RULE))

    def get_section_form(self, section_name):
        if section_name == 'Remove/add':
            return self.browser.find_element(*self.CHECKBOX_EXAMPLE_FORM)
        return self.browser.find_element(*self.INPUT_EXAMPLE_FORM)

    def get_num_checkboxes_in_section(self, section_name):
        section_form = self.get_section_form(section_name)
        return len(section_form.find_elements(*self.INPUT))

    def get_num_inputs_in_section(self, section_name):
        section_form = self.get_section_form(section_name)
        return len(section_form.find_elements(*self.INPUT))

    def get_num_buttons_in_section(self, section_name):
        section_form = self.get_section_form(section_name)
        return len(section_form.find_elements(*self.BUTTON))

    def get_checkbox_label(self, section_name):
        checkbox = self.browser.find_element(*self.ALTERNATIVE_CHECKBOX)
        if (checkbox.tag_name != 'input'):            
            section_form = self.get_section_form(section_name)
            # The label is actually part of the parent div
            return section_form.find_element(*self.CHECKBOX_LABEL).text
        else:
            return checkbox.find_element(*self.PARENT).text

    def get_checkbox_checked_state(self, section_name):
        section_form = self.get_section_form(section_name)
        return section_form.find_element(*self.INPUT).get_attribute('checked') == 'checked'

    def get_button_text(self, section_name):
        section_form = self.get_section_form(section_name)
        return section_form.find_element(*self.BUTTON).text

    def get_input_text(self, section_name):
        section_form = self.get_section_form(section_name)
        return section_form.find_element(*self.INPUT).text

    def is_input_enabled(self, section_name):
        section_form = self.get_section_form(section_name)
        return section_form.find_element(*self.INPUT).is_enabled()

    def click_button_by_text(self, buttonText):
        self.BUTTON_BY_TEXT = (self.BUTTON_BY_TEXT[0], self.BUTTON_BY_TEXT[1].replace('%s', buttonText))
        self.browser.find_element(*self.BUTTON_BY_TEXT).click()

    def is_loading_bar_displayed(self):
        return self.browser.find_element(*self.LOADING_BAR).is_displayed()

    def get_loading_bar_label(self):
        return self.browser.find_element(*self.LOADING_BAR).text

    def wait_for_loading_bar_to_appear(self):
        loading_bar = self.browser.find_element(*self.LOADING_BAR)
        WebDriverWait(self.browser, 10).until(EC.visibility_of(loading_bar))

    def wait_for_loading_bar_to_disappear(self):
        loading_bar = self.browser.find_element(*self.LOADING_BAR)
        WebDriverWait(self.browser, 10).until(EC.invisibility_of_element(loading_bar))

    def get_message_text(self):
        return self.browser.find_element(*self.MESSAGE).text

