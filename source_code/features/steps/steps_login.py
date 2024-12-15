
from behave import given, when, then
from PyQt5.QtWidgets import QApplication
import sys
from login import LoginWindow

@given('the user enters username "admin" and password "1234"')
def step_impl(context):
    context.app = QApplication(sys.argv)
    context.window = LoginWindow()
    context.window.username_input.setText("admin")
    context.window.password_input.setText("1234")

@when('the user clicks the login button')
def step_impl(context):
    context.window.login_button.click()

@then('a success message "Login Successful" should be displayed')
def step_impl(context):
    assert context.window.msg_box.message_text == "Login Successful"

@given('the user enters username "user" and password "123"')
def step_impl(context):
    context.app = QApplication(sys.argv)
    context.window = LoginWindow()
    context.window.username_input.setText("user")
    context.window.password_input.setText("123")

@then('an error message "Wrong username or wrong password!" should be displayed')
def step_impl(context):
    assert context.window.msg_box.message_text == "Wrong username or wrong password!"

@given('the user enters an empty username and password')
def step_impl(context):
    context.app = QApplication(sys.argv)
    context.window = LoginWindow()
    context.window.username_input.setText("")
    context.window.password_input.setText("")

@then('an error message "Please enter username and password!" should be displayed')
def step_impl(context):
    assert context.window.msg_box.message_text == "Please enter username and password!"
