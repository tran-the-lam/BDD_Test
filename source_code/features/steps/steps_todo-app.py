
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given('I am on the to-do list page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://127.0.0.1:5000/')
    time.sleep(1)

@when('I enter "Buy groceries" in the task input')
def step_impl(context):
    input_box = context.browser.find_element(By.NAME, 'task')
    input_box.send_keys('Buy groceries')

@when('I press the "Add" button')
def step_impl(context):
    add_button = context.browser.find_element(By.XPATH, '//form/button')
    add_button.click()
    time.sleep(1)

@then('I should see "Buy groceries" in the list of tasks')
def step_impl(context):
    tasks = context.browser.find_elements(By.XPATH, '//ul/li')
    assert any('Buy groceries' in task.text for task in tasks)
    context.browser.quit()

@given('I have added "Complete homework" to the task list')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://127.0.0.1:5000/')
    input_box = context.browser.find_element(By.NAME, 'task')
    input_box.send_keys('Complete homework')
    add_button = context.browser.find_element(By.XPATH, '//form/button')
    add_button.click()
    time.sleep(1)

@when('I click on the "Delete" link next to "Complete homework"')
def step_impl(context):
    delete_link = context.browser.find_element(By.XPATH, '//ul/li[contains(text(), "Complete homework")]/a')
    delete_link.click()
    time.sleep(1)

@then('"Complete homework" should no longer be in the list of tasks')
def step_impl(context):
    tasks = context.browser.find_elements(By.XPATH, '//ul/li')
    assert not any('Complete homework' in task.text for task in tasks)
    context.browser.quit()
