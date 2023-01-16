from selenium.webdriver.common.by import By
from pytest_bdd_ui_automation.pages.base import BasePage
from selenium.webdriver.support.select import Select

class DropdownPage(BasePage):

	@property
	def PAGE_TITLE(self):
		return (By.TAG_NAME, 'h3')
	DROPDOWN_LIST = (By.TAG_NAME, 'select')

	def __init__(self, browser):
		self.browser = browser

	def get_page_title_text(self):
		return self.browser.find_element(*self.PAGE_TITLE).text

	def get_num_dropdowns(self):
		return len(self.browser.find_elements(*self.DROPDOWN_LIST))

	def get_current_dropdown_value(self):
		dropdown = Select(self.browser.find_element(*self.DROPDOWN_LIST))
		return dropdown.first_selected_option.text

	def get_dropdown_options(self):
		dropdown = Select(self.browser.find_element(*self.DROPDOWN_LIST))
		options = [option.text for option in dropdown.options]
		return options

	def get_dropdown_supports_multi_select(self):
		dropdown = Select(self.browser.find_element(*self.DROPDOWN_LIST))
		return dropdown.is_multiple != None

	def select_option_by_text(self, text):
		dropdown = Select(self.browser.find_element(*self.DROPDOWN_LIST))
		dropdown.select_by_visible_text(text)
	
	def select_option_by_index(self, index):
		dropdown = Select(self.browser.find_element(*self.DROPDOWN_LIST))
		dropdown.select_by_index(index)
		