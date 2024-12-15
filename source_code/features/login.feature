
Feature: User Login

  Scenario: Successful login with correct credentials
    Given the user enters username "admin" and password "1234"
    When the user clicks the login button
    Then a success message "Login Successful" should be displayed

  Scenario: Unsuccessful login with incorrect credentials
    Given the user enters username "user" and password "123"
    When the user clicks the login button
    Then an error message "Wrong username or wrong password!" should be displayed

  Scenario: Missing username or password
    Given the user enters an empty username and password
    When the user clicks the login button
    Then an error message "Please enter username and password!" should be displayed
