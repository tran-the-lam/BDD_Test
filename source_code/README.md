## Overall
- [Step 1: Code login program](#login-program)
- [Step 2: Update user story](#update-user-story)
- [Step 3: Gen .feature file from user story](#gen-bdd-from-user-story)
- [Step 4: Gen steps file from (user story and login code)](#gen-file-test)
- [Step 5: Fill body code from (steps file and login code)](#gen-complete-file-test)
- [Step 6: Run test](#run-test)

### Login program
#### How to run project:


    - cd source_code
    - python -m venv myenv
    - pip install -r requirements.txt
    - source myenv/bin/activate (Macos/linux)
    - python login.py

View the `login.py` file [here](./login.py)
Login screen:
![Login screen](./images/login_screen.png)
Login successful:
![Login screen](./images/login_success.png)
Login failed:
![Login screen](./images/login_failed.png)

### Update user story
Edit in [user-story.txt](./user-story.txt) file
Example: `As a user, I want to see a success message when I enter the correct username and password (username: admin, password: 1234) so that I know I have logged in successfully`

### Gen BDD from user story
    - python generate_bdd.py
Input: user_story, login code
Contents of the [output file](./features/user_story_1.feature): 
```
Feature: Login Functionality

  Scenario: Successful login with correct username and password
    Given the user is on the login screen
    When the user enters the username "admin"
    And the user enters the password "1234"
    And the user clicks the "Login" button
    Then the user should see a success message "Login Successful"

```
View the `generate_bdd.py` file [here](./generate_bdd.py)

### Gen file test
`python generate_step_definition.py`
View the `generate_step_definition.py` file [here](./generate_step_definition.py)
Contents of the [output file](./features/steps/user_story_1.py): 
```
from behave import given, when, then

@given('the login window is open')
def step_impl(context):
    # TODO: Implement step: the login window is open
    raise NotImplementedError(""" Step not implemented: the login window is open """)


@when('I enter the username "admin" and password "1234"')
def step_impl(context):
    # TODO: Implement step: I enter the username "admin" and password "1234"
    raise NotImplementedError(""" Step not implemented: I enter the username "admin" and password "1234" """)


@when('I click the "Login" button')
def step_impl(context):
    # TODO: Implement step: I click the "Login" button
    raise NotImplementedError(""" Step not implemented: I click the "Login" button """)


@then('I should see a success message "Login Successful"')
def step_impl(context):
    # TODO: Implement step: I should see a success message "Login Successful"
    raise NotImplementedError(""" Step not implemented: I should see a success message "Login Successful" """)
```

### Gen complete file test
`python generate_complete_step.py`
Input: feature file, step file
Content of the output file
```

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


```

### Run test
`behave`

Output:
```
(myenv) lamtt@lamtts-MacBook-Air source_code % behave 
Starting tests...
Feature: User Login # features/user_story_1.feature:2

  Scenario: Successful login with correct username and password  # features/user_story_1.feature:4
    Given the login window is open                               # features/steps/user_story_1.py:7 0.162s
    When I enter the username "admin" and password "1234"        # features/steps/user_story_1.py:13 0.000s
    And I click the "Login" button                               # features/steps/user_story_1.py:18 2.687s
    Then I should see a success message "Login Successful"       # features/steps/user_story_1.py:22 0.000s

Tests completed.
1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
4 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m2.848s
```
