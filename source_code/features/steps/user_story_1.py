
from behave import given, when, then
from PyQt5.QtWidgets import QApplication
from login import LoginWindow
import sys

@given('the login window is open')
def step_impl(context):
    context.app = QApplication(sys.argv)
    context.window = LoginWindow()
    context.window.show()

@when('I enter the username "admin" and password "1234"')
def step_impl(context):
    context.window.username_input.setText("admin")
    context.window.password_input.setText("1234")

@when('I click the "Login" button')
def step_impl(context):
    context.window.login_button.click()

@then('I should see a success message "Login Successful"')
def step_impl(context):
    assert context.window.msg_box.message_text == "Login Successful"

