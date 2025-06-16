
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the homepage')
def step_impl(context):
    context.driver.get("http://localhost:5173")

@when('I select the radio input with value "Clothing" in the category filter')
def step_impl(context):
    # # Open the filters if they are not already open
    # filter_toggle = context.driver.find_element(By.CSS_SELECTOR, ".lg\\:w-64 .flex-shrink-0 button")
    # filter_toggle.click()

    # Wait for the filters to be visible
    # WebDriverWait(context.driver, 10).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, ".lg\\:w-64 .flex-shrink-0"))
    # )

    # Select the "Clothing" category
    clothing_radio = context.driver.find_element(By.XPATH, "//input[@type='radio' and @value='Clothing']")
    clothing_radio.click()

@then('the page heading should update to "Clothing"')
def step_impl(context):
    # Wait for the heading to update
    WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h2.text-2xl.font-bold.text-gray-900"), "Clothing")
    )
    heading = context.driver.find_element(By.CSS_SELECTOR, "h2.text-2xl.font-bold.text-gray-900")
    assert heading.text == "Clothing"

@then('the product count should reflect the filtered results')
def step_impl(context):
    # Wait for the product count to update
    product_count_text = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.text-gray-600"))
    ).text

    # Extract the number of products from the text
    product_count = int(product_count_text.split()[0])
    
    # Verify that the product count is correct
    product_cards = context.driver.find_elements(By.CSS_SELECTOR, ".grid .bg-white.rounded-lg.shadow-md")
    assert len(product_cards) == product_count

