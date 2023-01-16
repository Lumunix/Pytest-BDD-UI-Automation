from pytest_bdd import scenarios, when, then, parsers
from pages.checkboxes import CheckboxesPage
from sttable import parse_str_table

scenarios('../features/checkboxes_page.feature')

ORDINALS = ['st', 'nd', 'rd', 'th']
CHECK_STATES = ['checked', 'unchecked']


@when('I click on the <ordinal> checkbox')
def click_checkbox(browser, ordinal):
    index = int(ordinal[0:len(ordinal)-2]) - 1
    assert isinstance(index, int)
    assert index >= 0
    CheckboxesPage(browser).click_checkbox(index)


@then(parsers.parse('the page title is "{title}"'))
def verify_page_title(browser, title):
    assert title == CheckboxesPage(browser).get_page_title_text()


@then(parsers.parse('the page contains {num:d} checkboxes'))
def verify_num_checkboxes(browser, num):
    assert isinstance(num, int)
    assert num == CheckboxesPage(browser).get_num_checkboxes()


@then(parsers.parse('the checkbox labels are\n{labels}'))
def verify_checkbox_labels(browser, datatable, labels):
    expected = parse_str_table(labels)
    for field in expected.fields:
        assert expected.columns[field] == CheckboxesPage(browser).get_checkbox_labels()


@then(parsers.parse('the {index:d}{ordinal} checkbox is {state}'))
def verify_checkbox_state(browser, index, ordinal, state):
    assert isinstance(index, int)
    assert index > 0
    assert ordinal in ORDINALS
    assert state in CHECK_STATES
    checked_state = CheckboxesPage(browser).get_checkbox_checked_state(index - 1)
    if state == 'checked':
        assert checked_state == True
    else:
        assert checked_state == False


@then('the <ordinal> checkbox is <state>')
def verify_checkbox_state(browser, ordinal, state):
    # assert isinstance(index, int)
    # assert index > 0
    # assert ordinal in ORDINALS
    index = int(ordinal[0:len(ordinal)-2]) -1 
    assert state in CHECK_STATES
    checked_state = CheckboxesPage(browser).get_checkbox_checked_state(index)
    if state == 'checked':
        assert checked_state == True
    else:
        assert checked_state == False

@then('the <ordinal> checkbox is <first_state>')
def verify_checkbox_first_state(browser, ordinal, first_state):
  verify_checkbox_state(browser, ordinal, first_state)

@then('the <ordinal> checkbox is <second_state>')
def verify_checkbox_second_state(browser, ordinal, second_state):
  verify_checkbox_state(browser, ordinal, second_state)