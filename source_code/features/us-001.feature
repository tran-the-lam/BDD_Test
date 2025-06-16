
Feature: User Login

  Scenario: User logs in successfully
    Given the user is on the application
    When the user clicks the "Sign In" button
    Then the login dialog should be displayed
    When the user enters email "john@example.com" into the email input
    And the user enters password "password123" into the password input
    And the user clicks the "Sign In" button in the dialog
    Then the login dialog should close
    And the "Sign In" button should be hidden
