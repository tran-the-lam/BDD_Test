
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the application')
def step_impl(context):
    context.driver.get("http://localhost:5173")

@when('I click on the "Sign In" button')
def step_impl(context):
    sign_in_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]"))
    )
    sign_in_button.click()

@then('the login dialog should be displayed')
def step_impl(context):
    auth_modal = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "fixed.inset-0.bg-black.bg-opacity-50"))
    )
    assert auth_modal.is_displayed()

@when('I enter "john@example.com" into the email field')
def step_impl(context):
    email_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "email"))
    )
    email_field.clear()
    email_field.send_keys("john@example.com")

@when('I enter "password123" into the password field')
def step_impl(context):
    password_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_field.clear()
    password_field.send_keys("password123")

@when('I click on the "Sign In" button within the dialog')
def step_impl(context):
    sign_in_button_dialog = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]"))
    )
    sign_in_button_dialog.click()

@then('the login dialog should close')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "fixed.inset-0.bg-black.bg-opacity-50"))
    )

@then('the "Sign In" button should not be visible')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.invisibility_of_element_located((By.XPATH, "//button[contains(text(), 'Sign In')]"))
    )

