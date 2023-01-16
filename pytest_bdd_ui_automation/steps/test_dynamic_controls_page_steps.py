import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.dynamic_controls import DynamicControlsPage
from sttable import parse_str_table

scenarios('../features/dynamic_controls_page.feature')
SECTIONS = ['Remove/add', 'Enable/disable']
# section = None


@pytest.fixture
def data():
    return {}


@given(parsers.parse('I have clicked the "{button_text}" button'))
def click_button_and_wait(browser, data, button_text):
    click_button(browser, data, button_text)
    DynamicControlsPage(browser).wait_for_loading_bar_to_appear()
    DynamicControlsPage(browser).wait_for_loading_bar_to_disappear()


@when(parsers.parse('I click the "{button_text}" button'))
def click_button(browser, data, button_text):
    if (button_text == 'Remove' or button_text == 'Add'):
        data['section'] = SECTIONS[0]
    else:
        data['section'] = SECTIONS[1]
    DynamicControlsPage(browser).click_button_by_text(button_text)


@then(parsers.parse('the page title is "{title}"'))
def verify_page_title(browser, title):
    assert title == DynamicControlsPage(browser).get_page_title_text()


@then(parsers.parse('the opening paragraph text is "{text}"'))
def verify_opening_paragraph_text(browser, text):
    assert text == DynamicControlsPage(browser).get_opening_paragraph_text()


@then(parsers.parse('the page is divided into {num:d} sections\n{sections}'))
def verify_section_headers(browser, datatable, num, sections):
    assert num == DynamicControlsPage(browser).get_num_sections()
    expected = parse_str_table(sections)
    for field in expected.fields:
        assert expected.columns[field] == DynamicControlsPage(
            browser).get_section_headers_text()


@then('there is a horizontal line between the sections')
def verify_horizontal_line_divides_sections(browser):
    # This doesn't actually prove the horizontal line lies between the two sections but for now checking such an
    #element is present is sufficient
    assert 1 == DynamicControlsPage(browser).get_num_horizontal_rules()


@then(parsers.parse('the {section_name} section contains {num_1:d} {control_type} and {num_2:d} button'))
def verify_section_controls(browser, data, section_name, num_1, control_type, num_2):
    assert section_name in SECTIONS
    assert control_type in ['checkbox', 'checkboxes',
                            'input control', 'input controls']
    data['section'] = section_name
    if control_type.startswith('checkbox'):
        assert num_1 == DynamicControlsPage(
            browser).get_num_checkboxes_in_section(section_name)
    else:
        assert num_1 == DynamicControlsPage(
            browser).get_num_inputs_in_section(section_name)
    assert num_2 == DynamicControlsPage(
        browser).get_num_buttons_in_section(section_name)


@then(parsers.parse('the checkbox label is "{text}"'))
def verify_checkbox_label(browser, data, text):
    assert text == DynamicControlsPage(
        browser).get_checkbox_label(data['section'])


@then(parsers.parse('the checkbox is {state}'))
def verify_checkbox_checked_state(browser, data, state):
    expected = False
    if state == 'checked':
        expected = True
    assert expected == DynamicControlsPage(
        browser).get_checkbox_checked_state(data['section'])


@given(parsers.parse('the button text is "{text}"'))
@then(parsers.parse('the button text is "{text}"'))
def verify_button_text(browser, data, text):
    assert text == DynamicControlsPage(
        browser).get_button_text(data['section'])


@then('the input control is blank')
def verify_input_control_blank(browser, data):
    assert '' == DynamicControlsPage(browser).get_input_text(data['section'])


@then(parsers.parse('the input control is {state}'))
def verify_input_control_status(browser, data, state):
    expected = True if state == 'enabled' else False
    assert expected == DynamicControlsPage(
        browser).is_input_enabled(data['section'])


@then('a loading bar is displayed')
def verify_loading_bar_displayed(browser):
    assert True == DynamicControlsPage(browser).is_loading_bar_displayed()


@then(parsers.parse('the loading bar has a label of "{label}"'))
def verify_loading_bar_label(browser, label):
    assert label == DynamicControlsPage(browser).get_loading_bar_label()


@then('after a few seconds the loading bar disappears')
def verify_loading_bar_disappears(browser):
    DynamicControlsPage(browser).wait_for_loading_bar_to_disappear()
    assert False == DynamicControlsPage(browser).is_loading_bar_displayed()


@then('the checkbox is no longer displayed')
def verify_checkbox_not_displayed(browser):
    assert 0 == DynamicControlsPage(
        browser).get_num_checkboxes_in_section('Remove/add')


@then(parsers.parse('an "{message}" message is displayed'))
def verify_message_text(browser, message):
    assert message == DynamicControlsPage(browser).get_message_text()

@then('the checkbox is redisplayed')
def verify_checkbox_displayed(browser):
    assert 1 == DynamicControlsPage(
        browser).get_num_checkboxes_in_section('Remove/add')
