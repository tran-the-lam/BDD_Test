
Feature: User Login

  Scenario: Registered user logs in
    Given the user opens the application
    When the user clicks on the "Sign In" button
    Then the login dialog should be displayed
    When the user enters "john@example.com" in the email input
    And the user enters "password123" in the password input
    And the user clicks on the "Sign In" button in the dialog
    Then the login dialog should close
    And the "Sign In" button should not be visible
