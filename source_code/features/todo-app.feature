
Feature: To-Do List Management

  Scenario: Add a new task to the list
    Given I am on the to-do list page
    When I enter "Buy groceries" in the task input
    And I press the "Add" button
    Then I should see "Buy groceries" in the list of tasks

  Scenario: Remove a completed task from the list
    Given I have added "Complete homework" to the task list
    When I click on the "Delete" link next to "Complete homework"
    Then "Complete homework" should no longer be in the list of tasks
