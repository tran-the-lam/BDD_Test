# from behave import given, when, then
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# @given('the user is on the homepage')
# def step_impl(context):
#     context.driver = webdriver.Chrome()
#     context.driver.get("http://localhost:5173")
#     WebDriverWait(context.driver, 10).until(
#         EC.presence_of_element_located((By.TAG_NAME, "body"))
#     )

# @when('the user clicks the "Sign In" button')
# def step_impl(context):
#     sign_in_button = WebDriverWait(context.driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign In']"))
#     )
#     sign_in_button.click()

# @then('the login dialog should be displayed')
# def step_impl(context):
#     # Kiểm tra input email hiển thị là đủ
#     email_input = WebDriverWait(context.driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "email"))
#     )
#     assert email_input.is_displayed()

# @when('the user enters the email "john@example.com" into the email input field')
# def step_impl(context):
#     email_input = WebDriverWait(context.driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "email"))
#     )
#     email_input.clear()
#     email_input.send_keys("john@example.com")

# @when('the user enters the password "password123" into the password input field')
# def step_impl(context):
#     password_input = WebDriverWait(context.driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "password"))
#     )
#     password_input.clear()
#     password_input.send_keys("password123")

# @when('the user clicks the "Sign In" button in the login dialog')
# def step_impl(context):
#     sign_in_button_dialog = WebDriverWait(context.driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and text()='Sign In']"))
#     )
#     sign_in_button_dialog.click()

# @then('the login dialog should close')
# def step_impl(context):
#     WebDriverWait(context.driver, 10).until(
#         EC.invisibility_of_element_located((By.ID, "email"))
#     )

# @then('the "Sign In" button should not be visible')
# def step_impl(context):
#     sign_in_button = context.driver.find_elements(By.XPATH, "//button[text()='Sign In']")
#     assert len(sign_in_button) == 0 or not sign_in_button[0].is_displayed()

# def after_scenario(context, scenario):
#     context.driver.quit()
