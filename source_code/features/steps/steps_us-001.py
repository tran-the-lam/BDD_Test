
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the user is on the application')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5173")
    context.driver.maximize_window()

@when('the user clicks the "Sign In" button')
def step_impl(context):
    sign_in_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]"))
    )
    sign_in_button.click()

@then('the login dialog should be displayed')
def step_impl(context):
    login_dialog = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Sign In')]"))
    )
    assert login_dialog.is_displayed()

@when('the user enters email "john@example.com" into the email input')
def step_impl(context):
    email_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "email"))
    )
    email_input.clear()
    email_input.send_keys("john@example.com")

@when('the user enters password "password123" into the password input')
def step_impl(context):
    password_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_input.clear()
    password_input.send_keys("password123")

@when('the user clicks the "Sign In" button in the dialog')
def step_impl(context):
    sign_in_dialog_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In') and @type='submit']"))
    )
    sign_in_dialog_button.click()

@then('the login dialog should close')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.invisibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Sign In')]"))
    )

@then('the "Sign In" button should be hidden')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.invisibility_of_element_located((By.XPATH, "//button[contains(text(), 'Sign In')]"))
    )
    context.driver.quit()
