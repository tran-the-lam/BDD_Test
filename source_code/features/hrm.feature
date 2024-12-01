
Feature: Employee Management

  Scenario: Add employee information and display in a table
    Given the application is open
    When I enter "101" in the ID field
    And I enter "John Doe" in the Name field
    And I enter "1990" in the Birth Year field
    And I click on the "Save" button
    Then I should see "101" in the table
    And I should see "John Doe" in the table
    And I should see "1990" in the table

  Scenario: Automatically clear input fields after saving
    Given the application is open
    When I enter "102" in the ID field
    And I enter "Jane Smith" in the Name field
    And I enter "1985" in the Birth Year field
    And I click on the "Save" button
    Then the ID field should be empty
    And the Name field should be empty
    And the Birth Year field should be empty
