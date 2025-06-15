
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the user opens the application')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5173")

@when('the user clicks on the "Sign In" button')
def step_impl(context):
    sign_in_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign In']"))
    )
    sign_in_button.click()

@then('the login dialog should be displayed')
def step_impl(context):
    login_dialog = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "login-dialog"))
    )
    assert login_dialog.is_displayed()

@when('the user enters "john@example.com" in the email input')
def step_impl(context):
    email_input = context.driver.find_element(By.NAME, "email")
    email_input.clear()
    email_input.send_keys("john@example.com")

@when('the user enters "password123" in the password input')
def step_impl(context):
    password_input = context.driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys("password123")

@when('the user clicks on the "Sign In" button in the dialog')
def step_impl(context):
    dialog_sign_in_button = context.driver.find_element(By.XPATH, "//button[text()='Sign In']")
    dialog_sign_in_button.click()

@then('the login dialog should close')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "login-dialog"))
    )

@then('the "Sign In" button should not be visible')
def step_impl(context):
    sign_in_button = context.driver.find_elements(By.XPATH, "//button[text()='Sign In']")
    assert len(sign_in_button) == 0

def after_scenario(context, scenario):
    context.driver.quit()
