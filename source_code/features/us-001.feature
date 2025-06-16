
Feature: User login through the login dialog

  Scenario: User opens login dialog and logs in successfully
    Given the user is on the application
    When the user clicks the "Sign In" button
    Then the login dialog should be displayed
    When the user enters "john@example.com" in the email input field
    And the user enters "password123" in the password input field
    And the user clicks the "Sign In" button in the login dialog
    Then the login dialog should close
    And the "Sign In" button should no longer be visible
