from openai import OpenAI
from dotenv import load_dotenv
import os
import argparse

# https://apps.abacus.ai/chatllm/?convoId=120ee5e6e7&appId=2fef366f4
# TODO update prompt to load from all files in a directory

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()


def generate_complete_steps(original_path, step_path):
    with open(original_path, "r") as f:
        original_code = f.read()

    with open(step_path, "r") as f:
        step_code = f.read()

    prompt = f"""
        You are a Python expert. Your task is to complete the file `{step_path}` by implementing all the necessary parts based on the logic in `{original_path}`.

        ### Input Files:
        1. `{original_path}`: Contains the main logic for a specific functionality.
        2. `{step_path}`: Contains incomplete implementation or test steps related to `{original_path}`.

        ### Requirements:
        - Complete all missing steps in `{step_path}` based on the logic in `{original_path}`.
        - Ensure no scenario or step is missed.
        - Avoid repeating execution steps.
        - Handle multiple scenarios carefully, ensuring proper initialization to avoid conflicts.
        - Include all necessary imports and boilerplate code for the file to run correctly.
        - Return only the complete code for `{step_path}` without any explanation or comments.

        ### File Contents:
        #### `{original_path}`:
        {original_code}

        #### `{step_path}`:
        {step_code}

        ### Output:
        Return the complete `{step_path}` file with all steps implemented.
    """

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a Python expert."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
        max_tokens=3000,
    )

    content = completion.choices[0].message.content

    # Preprocess data before saving
    complete_steps = content.replace("```python", "")
    complete_steps = complete_steps.replace("```", "")

    # Write the complete steps to the file
    with open(step_path, "w") as f:
        f.write(complete_steps)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument("--task", type=str, help="The task to perform")

    # Parse the arguments
    args = parser.parse_args()

    original_path = f"{args.task}.py"
    step_path = f"features/steps/steps_{args.task}.py"
    generate_complete_steps(original_path, step_path)
