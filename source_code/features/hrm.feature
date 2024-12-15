
Feature: Employee Management

  Scenario: Add employee information and display in a table
    Given I am on the Employee Management application
    When I enter employee information with ID "101", Name "John Doe", Birth Year "1990"
    And I click the "Save" button
    Then the employee information should be displayed in the table
    And the table should contain one row with ID "101", Name "John Doe", Birth Year "1990"

  Scenario: Clear input fields after saving employee information
    Given I am on the Employee Management application
    When I enter employee information with ID "102", Name "Jane Smith", Birth Year "1992"
    And I click the "Save" button
    Then the input fields should be cleared
    And the input ID field should be empty
    And the input Name field should be empty
    And the input Birth Year field should be empty
