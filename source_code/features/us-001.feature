
Feature: User Login via Sign In Dialog

  Scenario: Registered user logs in successfully through the Sign In dialog
    Given the "Sign In" button is visible
    When the user clicks the "Sign In" button
    Then the login dialog is displayed
    When the user enters "john@example.com" into the email input
    And the user enters "password123" into the password input
    And the user clicks the "Sign In" button within the dialog
    Then the login dialog is closed
    And the "Sign In" button is no longer visible
