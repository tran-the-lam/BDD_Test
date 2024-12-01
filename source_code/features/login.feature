
Feature: Login functionality

  Scenario: Successful login with correct credentials
    Given I am on the login screen
    When I enter the username "admin" and password "1234"
    And I click the "Login" button
    Then I should see a success message "Login Successful"

  Scenario: Unsuccessful login with incorrect credentials
    Given I am on the login screen
    When I enter the username "user" and password "123"
    And I click the "Login" button
    Then I should see an error message "Wrong username or wrong password!"

  Scenario: Unsuccessful login with empty credentials
    Given I am on the login screen
    When I leave the username and password fields empty
    And I click the "Login" button
    Then I should see an error message "Please enter username and password!"
