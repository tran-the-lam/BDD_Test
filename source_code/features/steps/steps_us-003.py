
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am viewing a product card')
def step_impl(context):
    context.driver.get("http://localhost:5173")
    # Wait for the product grid to load and select the first product card
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="product-card"]'))
    )
    product_cards = context.driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')
    context.product_card = product_cards[0]

@when('I click the "Add to Cart" button')
def step_impl(context):
    add_to_cart_button = context.product_card.find_element(By.CSS_SELECTOR, '[data-testid="add-to-cart-button"]')
    add_to_cart_button.click()

@then('the cart icon counter should increase')
def step_impl(context):
    # sleep(3)
    from time import sleep
    sleep(5)
    
    # Wait for the cart item count to update
    WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-testid="cart-item-count"]'), '1')
    )
    cart_item_count = context.driver.find_element(By.CSS_SELECTOR, '[data-testid="cart-item-count"]')
    assert int(cart_item_count.get_attribute('data-count')) > 0

