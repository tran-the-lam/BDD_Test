from openai import OpenAI
from dotenv import load_dotenv
import os
import argparse
import json

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def generate_bdd_from_user_story(user_story, data_code):
    us_prompt = f"""
       Generate a `.feature` file using Gherkin syntax based on the following source code and user story. Prioritize the behavior and UI patterns directly inferred from the source code. Use the user story to support or fill in missing intent, but do not override or assume UI elements not present in the code.

        Key rules:
        - Do NOT assume the existence of pages, screens, or UI layouts unless clearly implemented in the code.
        - If the login is implemented as a dialog/modal (e.g., via `MatDialog`, `ModalComponent`, etc.), reflect that exactly in the Gherkin steps.
        - Use specific element names, labels, or selectors found in the code when describing `Given`, `When`, `Then` steps.
        - Only output the content of the `.feature` file – no extra text or explanation.

        User Story:
        {user_story}

        Source Code:
        {data_code}       
        
        Source Code Language: React 
    """
    
    completion = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """
                    You are a test automation assistant that specializes in generating `.feature` files using Gherkin syntax. Your primary responsibility is to infer real behaviors and UI interactions based on source code.

                    Guiding principles:
                    - Always prioritize behavior directly observed in the source code.
                    - Only use selectors (id, class, text, etc.) that actually exist in the provided code. If no id is present, use className or button text for locating elements.
                    - Treat user stories as supplemental context, but never override the code implementation with assumptions.
                    - Accurately identify the UI structure: if the code uses a modal/dialog for login, do not refer to it as a login page.
                    - Use identifiers, element names, and component types as seen in the code.
                    - Output strictly Gherkin syntax, no additional commentary or explanation.

                    You understand UI frameworks such as Angular, React, and can distinguish between components like pages, dialogs, modals, and services based on code patterns.
                """,
            },
            {"role": "user", "content": us_prompt},
        ],
    )
    return completion.choices[0].message.content

map_file_to_content = {}

def read_all_file_in_folder(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            if not file_name.endswith(".tsx") and not file_name.endswith(".ts"):
                continue
            with open(file_path, 'r') as file:
                content = file.read()
                map_file_to_content[file_path] = content
        elif os.path.isdir(file_path):
            read_all_file_in_folder(file_path)

def get_related_code(us_id, mapping_file="ecommerce/US_CODE.json"):
    """
    Trả về đoạn code liên quan đến user story.
    """
    related_code = ""
    # Đọc file mapping
    with open(mapping_file, "r") as f:
        us_code_map = json.load(f)
    # Lấy danh sách file liên quan đến user story
    file_list = us_code_map.get(us_id, [])
    for file_path in file_list:
        if file_path in map_file_to_content:
            related_code += f"##### {file_path}:\n{map_file_to_content[file_path]}\n\n"
    return related_code

if __name__ == "__main__":
    # Đọc user stories
    us_path = "ecommerce/USER_STORIES.md"
    with open(us_path, "r") as file:
        user_stories = file.readlines()
    
    # Tạo thư mục features nếu chưa có
    os.makedirs("features", exist_ok=True)

    # Sinh từng file feature cho từng user story (theo thứ tự)
    for line in user_stories:
        line = line.strip()
        if not line or not line.startswith("US-"):
            continue
        us_id = line.split(":")[0].strip()
        feature_filename = f"features/{us_id.lower()}.feature"
        data_code = get_related_code(us_id)  # chỉ lấy code liên quan
        bdd_scenarios = generate_bdd_from_user_story(line, data_code)
        bdd_scenarios = bdd_scenarios.replace("```gherkin", "").replace("```", "")
        with open(feature_filename, "w") as feature_file:
            feature_file.write(bdd_scenarios)
