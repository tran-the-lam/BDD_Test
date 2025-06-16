from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am viewing a product card with an "Add to Cart" button')
def step_impl(context):
    context.driver.get("http://localhost:5173")
    wait = WebDriverWait(context.driver, 10)
    # Wait for product cards to be visible
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="product-card"]')))
    # Find a product card with an enabled "Add to Cart" button
    product_cards = context.driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')
    for card in product_cards:
        try:
            add_to_cart_button = card.find_element(By.CSS_SELECTOR, 'button[data-testid="add-to-cart-button"]')
            if add_to_cart_button.is_enabled():
                context.product_card = card
                context.add_to_cart_button = add_to_cart_button
                return
        except:
            continue
    assert False, 'No product card with enabled "Add to Cart" button found'

@given('the cart icon counter is "0"')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    # Wait for cart button to be present
    cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="cart-button"]')))
    # Check if cart item count badge is present
    try:
        count_badge = cart_button.find_element(By.CSS_SELECTOR, '[data-testid="cart-item-count"]')
        count = count_badge.get_attribute("data-count")
        assert count == "0", f'Expected cart count to be "0" but got "{count}"'
    except:
        # No badge means zero items
        pass

@when('I click the "Add to Cart" button on the product card')
def step_impl(context):
    context.add_to_cart_button.click()

@then('the cart icon counter should increase by 1')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="cart-button"]')))
    def cart_count_is_one(driver):
        try:
            count_badge = cart_button.find_element(By.CSS_SELECTOR, '[data-testid="cart-item-count"]')
            count = count_badge.get_attribute("data-count")
            return count == "1"
        except:
            return False
    wait.until(cart_count_is_one)
    count_badge = cart_button.find_element(By.CSS_SELECTOR, '[data-testid="cart-item-count"]')
    count = count_badge.get_attribute("data-count")
    assert count == "1", f'Expected cart count to be "1" but got "{count}"'