Feature: Dynamic Controls Page

    Background: Open Dynamic Controls page
        Given I have navigated to the 'the-internet' "Dynamic Controls" page

    Scenario: Verify Dynamic Controls page contents are correct
        Then the page title is "Dynamic Controls"
        And the opening paragraph text is "This example demonstrates when elements (e.g., checkbox, input field, etc.) are changed asynchronously."
        And the page is divided into 2 sections
            | section        |
            | Remove/add     |
            | Enable/disable |
        And there is a horizontal line between the sections
        And the Remove/add section contains 1 checkbox and 1 button
        And the checkbox label is "A checkbox"
        And the checkbox is unchecked
        And the button text is "Remove"
        And the Enable/disable section contains 1 input control and 1 button
        And the input control is blank
        And the input control is disabled
        And the button text is "Enable"
        And a "Fork me on GitHub" banner is displayed in the top-right corner of the page
        And the page has a footer containing "Powered by Elemental Selenium"
        And the link in the page footer goes to "http://elementalselenium.com/"

    Scenario: Click Remove button
        When I click the "Remove" button
        Then a loading bar is displayed
        And the loading bar has a label of "Wait for it..."
        And after a few seconds the loading bar disappears
        And the checkbox is no longer displayed
        And the button text is "Add"
        And an "It's gone!" message is displayed

    Scenario: Click Add button
        Given I have clicked the "Remove" button
        And the button text is "Add"
        When I click the "Add" button
        Then a loading bar is displayed
        And the loading bar has a label of "Wait for it..."
        And after a few seconds the loading bar disappears
        And the checkbox is redisplayed
        And the checkbox label is "A checkbox"
        And the checkbox is unchecked
        And the button text is "Remove"
        And an "It's back!" message is displayed

    Scenario: Click Enable button
        When I click the "Enable" button
        Then a loading bar is displayed
        And the loading bar has a label of "Wait for it..."
        And after a few seconds the loading bar disappears
        And the input control is enabled
        And the button text is "Disable"
        And an "It's enabled!" message is displayed

    Scenario: Click Disable button
        Given I have clicked the "Enable" button
        And the button text is "Disable"
        When I click the "Disable" button
        Then a loading bar is displayed
        And the loading bar has a label of "Wait for it..."
        And after a few seconds the loading bar disappears
        And the input control is disabled
        And the button text is "Enable"
        And an "It's disabled!" message is displayed