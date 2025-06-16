
Feature: User Login

  Scenario: Successful login with valid credentials
    Given I am on the application
    When I click on the "Sign In" button
    Then the login dialog should be displayed
    When I enter "john@example.com" into the email field
    And I enter "password123" into the password field
    And I click on the "Sign In" button within the dialog
    Then the login dialog should close
    And the "Sign In" button should not be visible
