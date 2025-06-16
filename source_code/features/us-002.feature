
Feature: Filter product list by category

  Scenario: User selects the "Clothing" category filter
    Given the user is on the homepage
    When the user selects the radio input with value "Clothing" in the category filter
    Then the product list should update to show only clothing items
