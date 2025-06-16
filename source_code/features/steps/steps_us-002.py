
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the homepage')
def step_impl(context):
    context.driver.get("http://localhost:5173")
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "min-h-screen"))
    )

@when('I select the radio input with value "Clothing" in the category filter')
def step_impl(context):
    # filter_button = WebDriverWait(context.driver, 10).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, ".lg\\:w-64 .flex-shrink-0"))
    # )
    # filter_button.click()

    clothing_radio = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @value='Clothing']"))
    )
    clothing_radio.click()

@then('the page heading should update to "Clothing"')
def step_impl(context):
    heading = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h2.text-2xl.font-bold.text-gray-900"))
    )
    assert heading.text == "Clothing"

@then('the product count should reflect the filtered results')
def step_impl(context):
    product_count_text = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p.text-gray-600"))
    )
    product_count = int(product_count_text.text.split()[0])
    
    product_cards = context.driver.find_elements(By.CSS_SELECTOR, "[data-testid='product-card']")
    assert len(product_cards) == product_count

