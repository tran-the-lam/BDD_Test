
Feature: Add product to cart

  Scenario: User adds a product to the cart
    Given I am viewing a product card
    When I click the "Add to Cart" button
    Then the cart icon counter should increase
