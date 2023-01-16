from pytest_bdd import scenarios, when, then, parsers
from pages.home import HomePage
from pages.base import BasePage
from sttable import parse_str_table

scenarios('../features/home_page.feature')


@when('I click on the <page> link')
def click_page_link(browser, page):
    HomePage(browser).click_page_link(page)


@then(parsers.parse('the page title is "{title}"'))
def verify_page_title(browser, title):
    assert title == HomePage(browser).get_page_title_text()


@then(parsers.parse('the sub-header text is "{text}"'))
def verify_subheader_text(browser, text):
    assert text == HomePage(browser).get_subheader_text()


@then(parsers.parse('a list of the following sub-pages is displayed\n{subpages}'))
def verify_subpage_list(browser, datatable, subpages):
    expected = parse_str_table(subpages)
    for field in expected.fields:
        assert expected.columns[field] == HomePage(browser).get_subpage_list()

@then('the <page> page opens')
def verify_page_opens(browser, page):
    assert BasePage.PAGE_URLS.get(page.lower()) == HomePage(browser).get_current_url()