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


def generate_complete_steps(src_folder, step_path):
    # with open(original_path, "r") as f:
    #     original_code = f.read()

    with open(step_path, "r") as f:
        step_code = f.read()
        
    data_code = ""
    for k, v in map_file_to_content.items():
        data_code += f"##### {k}:\n{v}\n\n"

    prompt = f"""
        You are a Python expert. Your task is to complete the file `{step_path}` by implementing all the necessary parts based on the logic in `{src_folder}`.

        ### Input Files:
        1. `{src_folder}`: Contains the main logic for a specific program.
        2. `{step_path}`: Contains incomplete implementation or test steps related to `{src_folder}`.

        ### Requirements:
        - Complete all missing steps in `{step_path}` based on the logic in `{src_folder}`.
        - Ensure no scenario or step is missed.
        - Avoid repeating execution steps.
        - Handle multiple scenarios carefully, ensuring proper initialization to avoid conflicts.
        - Include all necessary imports and boilerplate code for the file to run correctly.
        - Return only the complete code for `{step_path}` without any explanation or comments.

        ### File Contents:
        #### `{src_folder}`:
        {data_code}

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

map_file_to_content = {}

def read_all_file_in_folder(folder_path):
    # List all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
                map_file_to_content[file_path] = content
        elif os.path.isdir(file_path):
            read_all_file_in_folder(file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument("--task", type=str, help="The task to perform", default="todo-app")
    parser.add_argument("--folder", type=str, help="The folder to read files from", default="todo-app")

    # Parse the arguments
    args = parser.parse_args()

    # original_path = f"{args.task}.py"
    step_path = f"features/steps/steps_{args.task}.py"

    read_all_file_in_folder(args.folder)
    generate_complete_steps(args.folder, step_path)
    
    
    print("Result====", map_file_to_content)