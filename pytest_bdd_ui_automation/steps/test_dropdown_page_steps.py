from pytest_bdd import scenarios, when, then, parsers
from pages.dropdown import DropdownPage
from sttable import parse_str_table

scenarios('../features/dropdown_page.feature')


@when('I select "<option_text>" from the dropdown list')
def select_dropdown_option_by_text(browser, option_text):
    DropdownPage(browser).select_option_by_text(option_text)


@when(parsers.parse('I select the {ordinal} option from the dropdown list'))
def select_dropdown_option_by_index(browser, ordinal):
    index = int(ordinal[0:len(ordinal)-2])
    DropdownPage(browser).select_option_by_index(index)


@then(parsers.parse('the page title is "{title}"'))
def verify_page_title(browser, title):
    assert title == DropdownPage(browser).get_page_title_text()


@then(parsers.parse('the page contains {num:d} dropdown list control'))
def verify_num_dropdowns(browser, num):
    assert isinstance(num, int)
    assert num == DropdownPage(browser).get_num_dropdowns()


@then(parsers.parse('the dropdown defaults to "{text}"'))
def verify_default_dropdown_option(browser, text):
    assert text == DropdownPage(browser).get_current_dropdown_value()


@then(parsers.parse('the dropdown contains the following options\n{options}'))
def verify_dropdown_options(browser, datatable, options):
    expected = parse_str_table(options)
    for field in expected.fields:
        assert expected.columns[field] == DropdownPage(
            browser).get_dropdown_options()


@then('the dropdown only support selection of a single option at a time')
def verify_only_single_selection(browser):
    assert False == DropdownPage(browser).get_dropdown_supports_multi_select()


@then('the dropdown value is "<option_text>"')
@then(parsers.parse('the dropdown value is "{option_text}"'))
def verify_selected_option(browser, option_text):
    assert option_text == DropdownPage(browser).get_current_dropdown_value()
