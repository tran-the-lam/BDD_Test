
Feature: Login Functionality

  Scenario: Successful login with correct credentials
    Given I am on the login screen
    When I enter "admin" as the username
    And I enter "1234" as the password
    And I click the "Login" button
    Then I should see a success message "Login Successful"

  Scenario: Unsuccessful login with incorrect credentials
    Given I am on the login screen
    When I enter "user" as the username
    And I enter "123" as the password
    And I click the "Login" button
    Then I should see an error message "Wrong username or wrong password!"

  Scenario: Unsuccessful login with empty credentials
    Given I am on the login screen
    When I leave the username empty
    And I leave the password empty
    And I click the "Login" button
    Then I should see an error message "Please enter username and password!"
