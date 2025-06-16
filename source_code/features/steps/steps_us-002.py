
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the user is on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5173")
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "min-h-screen"))
    )

@when('the user selects the radio input with value "Clothing" in the category filter')
def step_impl(context):
    filter_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Filters')]"))
    )
    filter_button.click()

    clothing_radio = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @value='Clothing']"))
    )
    clothing_radio.click()

@then('the product list should update to show only clothing items')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h2[@class='text-2xl font-bold text-gray-900']"), "Clothing")
    )
    products = context.driver.find_elements(By.CLASS_NAME, "product-card")
    for product in products:
        category = product.find_element(By.CLASS_NAME, "product-category").text
        assert category == "Clothing", f"Expected category 'Clothing', but got '{category}'"

    context.driver.quit()
