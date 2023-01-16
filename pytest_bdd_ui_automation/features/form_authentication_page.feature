Feature: Form Authentication Page

  Background: Open Form Authentication page
    Given I have navigated to the 'the-internet' "Form Authentication" page

  Scenario: Verify Form Authentication page contents are correct
    Then the page title is "Login Page"
    And the opening paragraph text is
      """
      This is where you can log into the secure area. Enter tomsmith for the username and
      SuperSecretPassword! for the password. If the information is wrong you should see error
      messages.
      """
    And a Username input is displayed
    And a Password input is displayed
    And a Login button is displayed
    And a "Fork me on GitHub" banner is displayed in the top-right corner of the page
    And the page has a footer containing "Powered by Elemental Selenium"
    And the link in the page footer goes to "http://elementalselenium.com/"

  Scenario: Login without user credentials
    When I click the Login button
    Then a red "Your username is invalid!" message banner is displayed

  Scenario: Login with valid username but no password
    When I enter a Username of "tomsmith"
    And I click the Login button
    Then a red "Your password is invalid!" message banner is displayed

  Scenario: Login with valid password but no username
    When I enter a Password of "SuperSecretPassword!"
    And I click the Login button
    Then a red "Your username is invalid!" message banner is displayed

  Scenario: Login with valid username but invalid password
    When I enter a Username of "tomsmith"
    And I enter a Password of "invalidPassword"
    And I click the Login button
    Then a red "Your password is invalid!" message banner is displayed

  Scenario: Login with valid password but invalid username
    When I enter a Username of "invalidUsername"
    And I enter a Password of "SuperSecretPassword!"
    And I click the Login button
    Then a red "Your username is invalid!" message banner is displayed

  Scenario: Login with valid credentials
    When I enter a Username of "tomsmith"
    And I enter a Password of "SuperSecretPassword!"
    And I click the Login button
    Then the "Secure Area" page opens
    And a green "You logged into a secure area!" message banner is displayed
    And the page title is "Secure Area"
    And the opening paragraph text is
      """
      Welcome to the Secure Area. When you are done click logout below.
      """
    And a Logout button is displayed
    And a "Fork me on GitHub" banner is displayed in the top-right corner of the page
    And the page has a footer containing "Powered by Elemental Selenium"
    And the link in the page footer goes to "http://elementalselenium.com/"