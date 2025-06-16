
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the user is on the application')
def step_impl(context):
    context.driver.get("http://localhost:5173")

@when('the user clicks the "Sign In" button')
def step_impl(context):
    sign_in_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="sign-in-button"]'))
    )
    sign_in_button.click()

@then('the login dialog should be displayed')
def step_impl(context):
    auth_modal = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.fixed.inset-0.bg-black.bg-opacity-50'))
    )
    assert auth_modal.is_displayed()

@when('the user enters "john@example.com" in the email input field')
def step_impl(context):
    email_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'email'))
    )
    email_input.clear()
    email_input.send_keys("john@example.com")

@when('the user enters "password123" in the password input field')
def step_impl(context):
    password_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'password'))
    )
    password_input.clear()
    password_input.send_keys("password123")

@when('the user clicks the "Sign In" button in the login dialog')
def step_impl(context):
    sign_in_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.w-full.bg-blue-600.text-white.py-2.rounded-lg'))
    )
    sign_in_button.click()

@then('the login dialog should close')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, '.fixed.inset-0.bg-black.bg-opacity-50'))
    )

@then('the "Sign In" button should no longer be visible')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, '[data-testid="sign-in-button"]'))
    )

