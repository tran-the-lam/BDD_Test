
Feature: User Login

  Scenario: Successful login with correct username and password
    Given the login window is open
    When I enter the username "admin" and password "1234"
    And I click the "Login" button
    Then I should see a success message "Login Successful"
