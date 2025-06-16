
Feature: Product Category Filter

  Scenario: Select category filter for Clothing
    Given I am on the homepage
    When I select the radio input with value "Clothing" in the category filter
    Then the page heading should update to "Clothing"
    And the product count should reflect the filtered results
