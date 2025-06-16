
Feature: Add product to cart

  Scenario: Adding a product to the cart increases the cart icon counter
    Given I am viewing a product card with an "Add to Cart" button
    And the cart icon counter is "0"
    When I click the "Add to Cart" button on the product card
    Then the cart icon counter should increase by 1
