from openai import OpenAI
from dotenv import load_dotenv
import os
import argparse

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()


def generate_complete_steps(src_folder, step_path):
    # Đọc code step hiện tại (nếu có)
    if os.path.exists(step_path):
        with open(step_path, "r") as f:
            step_code = f.read()
    else:
        step_code = ""
        
    data_code = ""
    for k, v in map_file_to_content.items():
        data_code += f"##### {k}:\n{v}\n\n"

    prompt = f"""
        You are a Python Selenium testing expert. Your task is to generate a complete Selenium test file `{step_path}` to test the web application's UI in `{src_folder}`.

        ### Input Files:
        1. `{src_folder}`: Contains the main logic for a specific program.
        2. `{step_path}`: Contains incomplete implementation or test steps related to `{src_folder}`.

        ### Requirements:
        - Use Python Selenium to automate browser actions.
        - Complete all missing steps in `{step_path}` based on the logic in `{src_folder}`.
        - Ensure no scenario or step is missed.
        - Avoid repeating execution steps.
        - Assume the web app is running locally (http://localhost:5173).
        - Handle multiple scenarios carefully, ensuring proper initialization to avoid conflicts.
        - Include all necessary imports and boilerplate code for the file to run correctly.
        - Return only the complete code for `{step_path}` without any explanation or comments.
        - Only use selectors (id, class, text, etc.) that actually exist in the provided code. If no id is present, use className or button text for locating elements.
        
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
            {"role": "system", "content": "You are a Code/QA expert."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
        max_tokens=16384,
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
        if not file_path.endswith(".tsx") and not file_path.endswith(".ts"):
            continue  # Skip files that are not .tsx and .ts
    
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
                map_file_to_content[file_path] = content
        elif os.path.isdir(file_path):
            read_all_file_in_folder(file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument("--start", type=int, default=1, help="Start user story number (e.g., 1 for us-001)")
    parser.add_argument("--end", type=int, default=1, help="End user story number (e.g., 36 for us-036)")
    parser.add_argument("--folder", type=str, help="The folder to read files from", default="ecommerce/")

    # Parse the arguments
    args = parser.parse_args()

    read_all_file_in_folder(args.folder)

    # Sinh step cho từng user story theo tuần tự
    for i in range(args.start, args.end + 1):
        us_id = f"us-{i:03d}"
        step_path = f"features/steps/steps_{us_id}.py"
        generate_complete_steps(args.folder, step_path)