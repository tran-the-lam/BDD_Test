
Feature: User Login

  Scenario: Successful login using the login dialog
    Given I am a registered user
    When I click the "Sign In" button
    Then the login dialog should be displayed
    When I enter my email "john@example.com" in the email input field
    And I enter my password "password123" in the password input field
    And I click the "Sign In" button in the dialog
    Then the login dialog should close
    And the "Sign In" button should not be visible
