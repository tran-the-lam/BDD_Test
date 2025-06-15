
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am a registered user')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5173")
    context.driver.maximize_window()

@when('I click the "Sign In" button')
def step_impl(context):
    sign_in_button = context.driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In') and not(ancestor::form)]")
    sign_in_button.click()

@then('the login dialog should be displayed')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "email"))
    )

@when('I enter my email "john@example.com" in the email input field')
def step_impl(context):
    email_input = context.driver.find_element(By.ID, "email")
    email_input.send_keys("john@example.com")

@when('I enter my password "password123" in the password input field')
def step_impl(context):
    password_input = context.driver.find_element(By.ID, "password")
    password_input.send_keys("password123")

@when('I click the "Sign In" button in the dialog')
def step_impl(context):
    sign_in_dialog_button = context.driver.find_element(By.XPATH, "//form//button[contains(text(), 'Sign In')]")
    sign_in_dialog_button.click()

@then('the login dialog should close')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "email"))
    )

@then('the "Sign In" button should not be visible')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.invisibility_of_element_located((By.XPATH, "//button[contains(text(), 'Sign In') and not(ancestor::form)]"))
    )
    context.driver.quit()
