Feature: Checkboxes Page

  Background: Open Checkboxes page
    Given I have navigated to the 'the-internet' "Checkboxes" page

  Scenario: Verify Checkboxes page contents are correct
    Then the page title is "Checkboxes"
    And the page contains 2 checkboxes
    And the checkbox labels are
      | label      |
      | checkbox 1 |
      | checkbox 2 |
    And the 1st checkbox is unchecked
    And the 2nd checkbox is checked
    And a "Fork me on GitHub" banner is displayed in the top-right corner of the page
    And the page has a footer containing "Powered by Elemental Selenium"
    And the link in the page footer goes to "http://elementalselenium.com/"

  Scenario Outline: Click on <ordinal> checkbox
    When I click on the <ordinal> checkbox
    Then the <ordinal> checkbox is <state>
    Examples:
      | ordinal | state     |
      | 1st     | checked   |
      | 2nd     | unchecked |

Scenario Outline: Click on <ordinal> checkbox twice
  When I click on the <ordinal> checkbox
  Then the <ordinal> checkbox is <first_state>
  When I click on the <ordinal> checkbox
  Then the <ordinal> checkbox is <second_state>
  Examples:
    | ordinal | first_state | second_state |
    | 1st     | checked     | unchecked    |
    | 2nd     | unchecked   | checked      |