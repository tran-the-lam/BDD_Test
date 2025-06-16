from openai import OpenAI
from dotenv import load_dotenv
import os
import argparse
import json

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def get_related_code(us_id, mapping_file="ecommerce/US_CODE.json"):
    """
    Trả về đoạn code liên quan đến user story dựa trên file mapping.
    """
    related_code = ""
    if not os.path.exists(mapping_file):
        return related_code
    with open(mapping_file, "r") as f:
        us_code_map = json.load(f)
    file_list = us_code_map.get(us_id.upper(), [])
    for file_path in file_list:
        if os.path.exists(file_path):
            with open(file_path, "r") as code_file:
                related_code += f"##### {file_path}:\n{code_file.read()}\n\n"
    return related_code

def generate_complete_steps(us_id, data_code, step_path):
    # Đọc code step hiện tại (nếu có)
    if os.path.exists(step_path):
        with open(step_path, "r") as f:
            step_code = f.read()
    else:
        step_code = ""
        
    prompt = f"""
        You are a Python Selenium testing expert. Your task is to generate a complete Selenium test file `{step_path}` to test the web application's UI for user story {us_id}.

        ### General Requirements:
        - Use Python Selenium to automate browser actions.
        - Complete all missing steps in `{step_path}` based on the logic in the provided code and user story.
        - Ensure no scenario or step is missed.
        - Avoid repeating execution steps.
        - Assume the web app is running locally (http://localhost:5173).
        - Handle multiple scenarios carefully, ensuring proper initialization to avoid conflicts.
        - Include all necessary imports and boilerplate code for the file to run correctly.
        - Return only the complete code for `{step_path}` without any explanation or comments.

        ### Selector Guidelines:
        - Always use selectors (id, class, text, etc.) that actually exist in the provided code. Do NOT assume any id/class that does not exist.
        - If an element does not have an id, use className, button text, or other unique attributes for locating elements.
        - When there are multiple elements with the same label (e.g., multiple "Sign In" buttons), select the correct one based on its context in the DOM (e.g., header, dialog, form, etc.).
            - For example, to click a button in a dialog, ensure the button is a descendant of the dialog container or is the submit button of the login form.
            - To click a button on the main page (not in a dialog), ensure it is not a descendant of any dialog/modal container.
        - When verifying that a dialog/modal is displayed, check for the presence or visibility of a unique element inside the dialog (such as an input field or heading), not for a generic class/id unless it exists in the code.
        - Do NOT use ancestor or descendant selectors with class names that are not present in the code.

        ### Output:
        - Return the complete `{step_path}` file with all steps implemented, using only selectors and UI flows that are verifiable from the provided code.

        ### Related Source Code:
        {data_code}

        ### Existing Step File:
        {step_code}

        ### Output:
        Return the complete `{step_path}` file with all steps implemented.
    """
    
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a Python Selenium testing expert"},
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=1, help="Start user story number (e.g., 1 for us-001)")
    parser.add_argument("--end", type=int, default=2, help="End user story number (e.g., 36 for us-036)")
    # parser.add_argument("--mapping", type=str, default="us_code_mapping.json", help="Mapping file userstory to code")
    args = parser.parse_args()

    # Sinh step cho từng user story theo tuần tự
    for i in range(args.start, args.end + 1):
        us_id = f"US-{i:03d}"
        step_path = f"features/steps/steps_{us_id.lower()}.py"
        data_code = get_related_code(us_id)
        print(f"Generating steps for {us_id}...")
        if not data_code:
            print(f"No related code found for {us_id}. Skipping step generation.")
            continue
        # print("data_code:", data_code)
        generate_complete_steps(us_id, data_code, step_path)