
Feature: Category Filter on Homepage

  Scenario: Select "Clothing" category filter and see updated heading and product count
    Given I am on the homepage
    When I select the radio input with value "Clothing" in the category filter
    Then the page heading updates to "Clothing"
    And the product count updates to reflect the filtered results for "Clothing"
