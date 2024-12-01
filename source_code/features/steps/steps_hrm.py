
from behave import given, when, then
from PyQt5.QtWidgets import QApplication
from hrm import EmployeeApp
import sys

@given('the application is open')
def step_impl(context):
    context.app = QApplication(sys.argv)
    context.window = EmployeeApp()
    context.window.show()

@when('I enter "{text}" in the ID field')
def step_impl(context, text):
    context.window.input_id.setText(text)

@when('I enter "{text}" in the Name field')
def step_impl(context, text):
    context.window.input_name.setText(text)

@when('I enter "{text}" in the Birth Year field')
def step_impl(context, text):
    context.window.input_birth_year.setText(text)

@when('I click on the "Save" button')
def step_impl(context):
    context.window.save_button.click()

@then('I should see "{text}" in the table')
def step_impl(context, text):
    found = False
    for row in range(context.window.table.rowCount()):
        for column in range(context.window.table.columnCount()):
            item = context.window.table.item(row, column)
            if item and item.text() == text:
                found = True
                break
    assert found, f"Text '{text}' not found in the table"

@then('the ID field should be empty')
def step_impl(context):
    assert context.window.input_id.text() == "", "ID field is not empty"

@then('the Name field should be empty')
def step_impl(context):
    assert context.window.input_name.text() == "", "Name field is not empty"

@then('the Birth Year field should be empty')
def step_impl(context):
    assert context.window.input_birth_year.text() == "", "Birth Year field is not empty"
