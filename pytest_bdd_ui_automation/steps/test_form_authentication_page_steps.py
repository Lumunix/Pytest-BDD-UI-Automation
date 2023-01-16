from pytest_bdd import scenarios, when, then, parsers
from pages.base import BasePage
from pages.form_authentication import FormAuthenticationPage

scenarios('../features/form_authentication_page.feature')


@when(parsers.parse('I enter a username of "{username}"'))
def enter_username(browser, username):
    FormAuthenticationPage(browser).enter_username(username)


@when(parsers.parse('I enter a password of "{password}"'))
def enter_password(browser, password):
    FormAuthenticationPage(browser).enter_password(password)


@when('I click the Login button')
def click_login_button(browser):
    FormAuthenticationPage(browser).click_login_button()


@then(parsers.parse('the page title is "{title}"'))
def verify_page_title(browser, title):
    assert title == FormAuthenticationPage(browser).get_page_title_text()


@then(parsers.parse('the opening paragraph text is\n{paragraph}'))
def verify_opening_paragraph_text(browser, paragraph):
    assert paragraph.replace('\n', ' ') == FormAuthenticationPage(
        browser).get_opening_paragraph_text()


@then(parsers.parse('a {input_type} input is displayed'))
def verify_input_displayed(browser, input_type):
    assert input_type in ['Username', 'Password']
    if input_type == 'Username':
        assert True == FormAuthenticationPage(
            browser).is_username_input_displayed()
        assert input_type == FormAuthenticationPage(
            browser).get_username_input_label_text()
    else:
        assert True == FormAuthenticationPage(
            browser).is_password_input_displayed()
        assert input_type == FormAuthenticationPage(
            browser).get_password_input_label_text()


@then('a Login button is displayed')
def verify_login_button_displayed(browser):
    assert True == FormAuthenticationPage(browser).is_login_button_displayed()
    assert 'Login' == FormAuthenticationPage(browser).get_login_button_text()


@then(parsers.parse('a {colour} "{message}" message banner is displayed'))
def verify_message_text_and_colour(browser, config, colour, message):
    assert colour in ['red', 'green']
    if config['browser'] == 'Firefox':
        expected_colour = 'rgb(198, 15, 19)' if colour == 'red' else 'rgb(93, 164, 35)'
    else:
        expected_colour = 'rgba(198, 15, 19, 1)' if colour == 'red' else 'rgba(93, 164, 35, 1)'
    assert True == FormAuthenticationPage(
        browser).is_message_banner_displayed()
    assert expected_colour == FormAuthenticationPage(
        browser).get_message_banner_colour()
    assert message == FormAuthenticationPage(browser).get_message_banner_text()


@then('a Logout button is displayed')
def verify_logout_button_displayed(browser):
    assert True == FormAuthenticationPage(browser).is_logout_button_displayed()
    assert 'Logout' == FormAuthenticationPage(browser).get_logout_button_text()

@then(parsers.parse('the "{page}" page opens'))
def verify_page_opens(browser, page):
    assert BasePage.PAGE_URLS.get(page.lower()) == FormAuthenticationPage(browser).get_current_url()
