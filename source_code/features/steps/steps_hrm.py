
from behave import given, when, then
from PyQt5.QtWidgets import QApplication
from hrm import EmployeeApp
import sys

@given('I am on the Employee Management application')
def step_impl(context):
    context.app = QApplication(sys.argv)
    context.window = EmployeeApp()
    context.window.show()

@when('I enter employee information with ID "101", Name "John Doe", Birth Year "1990"')
def step_impl(context):
    context.window.input_id.setText("101")
    context.window.input_name.setText("John Doe")
    context.window.input_birth_year.setText("1990")

@when('I click the "Save" button')
def step_impl(context):
    context.window.save_button.click()

@then('the employee information should be displayed in the table')
def step_impl(context):
    table = context.window.table
    assert table.rowCount() > 0

@then('the table should contain one row with ID "101", Name "John Doe", Birth Year "1990"')
def step_impl(context):
    table = context.window.table
    assert table.item(0, 0).text() == "101"
    assert table.item(0, 1).text() == "John Doe"
    assert table.item(0, 2).text() == "1990"

@when('I enter employee information with ID "102", Name "Jane Smith", Birth Year "1992"')
def step_impl(context):
    context.window.input_id.setText("102")
    context.window.input_name.setText("Jane Smith")
    context.window.input_birth_year.setText("1992")

@then('the input fields should be cleared')
def step_impl(context):
    assert context.window.input_id.text() == ""
    assert context.window.input_name.text() == ""
    assert context.window.input_birth_year.text() == ""

@then('the input ID field should be empty')
def step_impl(context):
    assert context.window.input_id.text() == ""

@then('the input Name field should be empty')
def step_impl(context):
    assert context.window.input_name.text() == ""

@then('the input Birth Year field should be empty')
def step_impl(context):
    assert context.window.input_birth_year.text() == ""
