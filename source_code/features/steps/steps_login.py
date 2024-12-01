
from behave import given, when, then
from PyQt5.QtWidgets import QApplication
from login import LoginWindow
import sys

@given('I am on the login screen')
def step_impl(context):
    context.app = QApplication(sys.argv)
    context.window = LoginWindow()
    context.window.show()

@when('I enter "admin" as the username')
def step_impl(context):
    context.window.username_input.setText("admin")

@when('I enter "1234" as the password')
def step_impl(context):
    context.window.password_input.setText("1234")

@when('I click the "Login" button')
def step_impl(context):
    context.window.login_button.click()

@then('I should see a success message "Login Successful"')
def step_impl(context):
    assert context.window.msg_box.message_text == "Login Successful"

@when('I enter "user" as the username')
def step_impl(context):
    context.window.username_input.setText("user")

@when('I enter "123" as the password')
def step_impl(context):
    context.window.password_input.setText("123")

@then('I should see an error message "Wrong username or wrong password!"')
def step_impl(context):
    assert context.window.msg_box.message_text == "Wrong username or wrong password!"

@when('I leave the username empty')
def step_impl(context):
    context.window.username_input.setText("")

@when('I leave the password empty')
def step_impl(context):
    context.window.password_input.setText("")

@then('I should see an error message "Please enter username and password!"')
def step_impl(context):
    assert context.window.msg_box.message_text == "Please enter username and password!"

