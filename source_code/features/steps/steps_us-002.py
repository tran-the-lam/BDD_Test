from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the homepage')
def step_impl(context):
    context.driver.get("http://localhost:5173")
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h2.text-2xl.font-bold.text-gray-900"))
    )

@when('I select the radio input with value "Clothing" in the category filter')
def step_impl(context):
    # The category filter radio inputs are inside the filters sidebar with label text matching category names
    # Locate the label with text "Clothing" and find the associated input
    labels = context.driver.find_elements(By.CSS_SELECTOR, "div.lg\\:w-64.flex-shrink-0 label")
    for label in labels:
        if label.text.strip() == "Clothing":
            # The input is a child of the label or associated by for attribute
            input_elem = label.find_element(By.CSS_SELECTOR, "input[type='radio']")
            if not input_elem.is_selected():
                input_elem.click()
            break
    else:
        assert False, 'Category radio input with value "Clothing" not found'

@then('the page heading updates to "Clothing"')
def step_impl(context):
    heading = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h2.text-2xl.font-bold.text-gray-900"))
    )
    assert heading.text == "Clothing", f'Expected heading to be "Clothing" but got "{heading.text}"'

@then('the product count updates to reflect the filtered results for "Clothing"')
def step_impl(context):
    # The product count is in a <p> with class text-gray-600 next to the heading
    count_p = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.flex.items-center.justify-between > p.text-gray-600"))
    )
    count_text = count_p.text.strip()
    # It should be like "X products found" or "1 product found"
    import re
    m = re.match(r"(\d+) product[s]? found", count_text)
    assert m, f'Product count text format unexpected: "{count_text}"'
    count = int(m.group(1))
    # Verify that the product grid shows exactly that many product cards
    product_cards = context.driver.find_elements(By.CSS_SELECTOR, "div[data-testid='product-card']")
    assert len(product_cards) == count, f'Product count text says {count} but found {len(product_cards)} product cards'
    # Additionally, verify that count is > 0 (since Clothing category should have products)
    assert count > 0, "Expected at least one product for category 'Clothing'"

