from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI()


def generate_complete_steps(login_code, steps_code):
    prompt = f"""
    You are a Python expert. I have a file `login.py` that contains the logic for a login system, and a file `login_steps.py` that contains incomplete test steps for Behave (BDD testing). Your task is to complete the `login_steps.py` file by implementing all the test steps based on the logic in `login.py`.

    Here is the content of `login.py`:
    {login_code}

    Here is the current content of `login_steps.py`:
    {steps_code}

    Please return the complete `login_steps.py` file with all steps implemented.
    Only code without explanation, note.
    Please check import libraries and other necessary code before running the code.
    """
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a Python expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    return completion.choices[0].message.content

# Read login.py
with open("login.py", "r") as f:
    login_code = f.read()

# Read steps/login_steps.py
with open("features/steps/user_story_1.py", "r") as f:
    steps_code = f.read()

# Send request to OpenAI to generate complete steps
complete_steps = generate_complete_steps(login_code, steps_code)

# Clear the generated data
complete_steps = complete_steps.replace("```python", "")
complete_steps = complete_steps.replace("```", "")

# Write the complete steps to steps/login_steps.py 
with open("features/steps/user_story_1.py", "w") as f:
    f.write(complete_steps)

print("The file features/steps/user_story_1.py has been updated with complete test steps.")