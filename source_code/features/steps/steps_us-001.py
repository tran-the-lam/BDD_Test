from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the "Sign In" button is visible')
def step_impl(context):
    context.driver.get("http://localhost:5173")
    sign_in_button = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="sign-in-button"]'))
    )
    assert sign_in_button.is_displayed()

@when('the user clicks the "Sign In" button')
def step_impl(context):
    sign_in_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="sign-in-button"]'))
    )
    sign_in_button.click()

@then('the login dialog is displayed')
def step_impl(context):
    login_dialog = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"fixed inset-0 bg-black bg-opacity-50")]'))
    )
    heading = context.driver.find_element(By.XPATH, '//h2[contains(text(),"Sign In")]')
    assert login_dialog.is_displayed()
    assert heading.is_displayed()

@when('the user enters "john@example.com" into the email input')
def step_impl(context):
    email_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#email'))
    )
    email_input.clear()
    email_input.send_keys("john@example.com")

@when('the user enters "password123" into the password input')
def step_impl(context):
    password_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#password'))
    )
    password_input.clear()
    password_input.send_keys("password123")

@when('the user clicks the "Sign In" button within the dialog')
def step_impl(context):
    # The submit button inside the dialog has text "Sign In"
    submit_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//form//button[@type="submit" and (text()="Sign In" or contains(text(),"Sign In"))]'))
    )
    submit_button.click()

@then('the login dialog is closed')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.invisibility_of_element_located((By.XPATH, '//div[contains(@class,"fixed inset-0 bg-black bg-opacity-50")]'))
    )
    dialogs = context.driver.find_elements(By.XPATH, '//div[contains(@class,"fixed inset-0 bg-black bg-opacity-50")]')
    assert len(dialogs) == 0 or all(not d.is_displayed() for d in dialogs)

@then('the "Sign In" button is no longer visible')
def step_impl(context):
    # The sign in button should not be visible after login
    sign_in_buttons = context.driver.find_elements(By.CSS_SELECTOR, 'button[data-testid="sign-in-button"]')
    assert len(sign_in_buttons) == 0 or all(not b.is_displayed() for b in sign_in_buttons)