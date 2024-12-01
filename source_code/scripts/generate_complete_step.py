from openai import OpenAI
from dotenv import load_dotenv
import os
import argparse

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI()


def generate_complete_steps(original_file_name, step_file_name):
    # prompt = f"""
    # You are a Python expert. I have a file `{original_file_name}` that contains the logic for a login system, and a file `login_steps.py` that contains incomplete test steps for Behave (BDD testing). Your task is to complete the `login_steps.py` file by implementing all the test steps based on the logic in `login.py`.

    # Here is the content of `login.py`:
    # {code}

    # Here is the current content of `login_steps.py`:
    # {code}

    # Please return the complete `login_steps.py` file with all steps implemented.
   
    # """
    
    with open(original_file_name, "r") as f:
        original_code = f.read()

    with open(step_file_name, "r") as f:
        step_code = f.read()
    
    prompt = f"""
    You are a Python expert. I have a file `{original_file_name}` that contains the main logic for a specific functionality, and a file `{step_file_name}` that contains incomplete implementation or test steps related to `{original_file_name}`. Your task is to complete the `{step_file_name}` file by implementing all the necessary parts based on the logic in `{original_file_name}`.

    Here is the content of `{original_file_name}`:
    {original_code}

    Here is the current content of `{step_file_name}`:
    {step_code}

    Please return the complete `{step_file_name}` file with all necessary implementations.
    Please check import libraries and other necessary code before running the code. 
    If there are multiple scenarios, pay attention to the initialization part to avoid conflicts.
    Only code without explanation or note.
    """
    
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a Python expert."},
            {"role": "user", "content": prompt}
        ],
        # temperature=0
    )
    
    content = completion.choices[0].message.content
    
    # Clear the generated data
    complete_steps = content.replace("```python", "")
    complete_steps = complete_steps.replace("```", "")
    
    # Write the complete steps to the file
    with open(step_file_name, "w") as f:
        f.write(complete_steps)
    





if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument("--code_path", type=str, help="The code path to generate steps")
    parser.add_argument("--prefix_output", type=str, help="The prefix of the feature file")
    
    # Parse the arguments
    args = parser.parse_args()
    
    generate_complete_steps(args.code_path, f"features/steps/steps_{args.prefix_output}.py")
    
