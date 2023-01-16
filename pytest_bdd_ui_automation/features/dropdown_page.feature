Feature: Dropdown Page

  Background: Open Dropdown page
    Given I have navigated to the 'the-internet' "Dropdown" page

  Scenario: Verify Dropdown page contents are correct
    Then the page title is "Dropdown List"
    And the page contains 1 dropdown list control
    And the dropdown defaults to "Please select an option"
    And the dropdown contains the following options
      | options                 |
      | Please select an option |
      | Option 1                |
      | Option 2                |
    And the dropdown only support selection of a single option at a time
    And a "Fork me on GitHub" banner is displayed in the top-right corner of the page
    And the page has a footer containing "Powered by Elemental Selenium"
    And the link in the page footer goes to "http://elementalselenium.com/"

  Scenario Outline: Select dropdown option by text
    When I select "<option_text>" from the dropdown list
    Then the dropdown value is "<option_text>"
    Examples:
      | option_text |
      | Option 1    |
      | Option 2    |

Scenario: Select dropdown options by index
  When I select the 2nd option from the dropdown list
  Then the dropdown value is "Option 2"
  When I select the 1st option from the dropdown list
  Then the dropdown value is "Option 1"