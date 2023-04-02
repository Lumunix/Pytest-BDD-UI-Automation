import pytest

from pytest_bdd import given, then, parsers
from pytest_bdd_ui_automation.pages.base import BasePage

@pytest.fixture
def datatable():
    return DataTable()


class DataTable(object):

    def __init__(self):
        pass

    def __str__(self):
        dt_str = ''
        for field, value in self.__dict__.items():
            dt_str = f'{dt_str}\n{field} = {value}'
        return dt_str

    def __repr__(self) -> str:
        return self.__str__()


@given(parsers.parse('I have navigated to the \'the-internet\' "{page_name}" page'), target_fixture='navigate_to')
def navigate_to(browser, page_name):
    url = BasePage.PAGE_URLS.get(page_name.lower())
    browser.get(url)


@then(parsers.parse('a "{text}" banner is displayed in the top-right corner of the page'))
def verify_banner_text(browser, text):
    url = 'https://github.com/tourdedave/the-internet'
    assert text == BasePage(browser).get_github_fork_banner_text()
    assert url == BasePage(browser).get_github_fork_banner_link()
    styleAttrs = BasePage(browser).get_github_fork_banner_position().split(";")
    for attr in styleAttrs:
        if attr.startswith("position"):
            assert "absolute" == attr.split(": ")[1]
        if attr.startswith("top"):
            assert "0px" == attr.split(": ")[1]
        if attr.startswith("right"):
            assert "0px" == attr.split(": ")[1]
        if attr.startswith("border"):
            assert "0px" == attr.split(": ")[1]


@then(parsers.parse('the page has a footer containing "{text}"'))
def verify_footer_text(browser, text):
    assert text == BasePage(browser).get_page_footer_text()


@then(parsers.parse('the link in the page footer goes to "{url}"'))
def verify_footer_link_url(browser, url):
    assert url == BasePage(browser).get_page_footer_link_url()