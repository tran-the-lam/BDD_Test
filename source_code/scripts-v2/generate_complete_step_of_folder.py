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

        ### Session Management (IMPORTANT):
        - DO NOT create new webdriver instances (e.g., context.driver = webdriver.Chrome()) in step definitions.
        - Assume the driver is already initialized via environment.py and available as context.driver.
        - DO NOT call context.driver.quit() anywhere in the step file.
        - For @given steps that navigate to pages, only use context.driver.get() if needed, but don't create new driver.
        - The browser session should persist between different test scenarios to maintain login state and other session data.

        ### Selector Guidelines:
        - Always use selectors (id, class, text, etc.) that actually exist in the provided code. Do NOT assume any id/class that does not exist.
        - Analyze the React/HTML structure carefully before choosing selectors:
          * If components use Tailwind CSS classes, use the actual Tailwind classes (e.g., "bg-white rounded-lg shadow-md")
          * If components use CSS modules or custom classes, use those exact class names
          * If no specific classes exist, use structural selectors (tag names, hierarchy, attributes)
        - Do NOT invent generic class names like ".product-card", ".category-label", ".modal-dialog" unless they appear in the source code
        - When checking filtered/updated content, verify:
          * Changes in headings or text content that reflect the action
          * Presence/absence of elements rather than specific labels that may not exist
          * Count or visibility of elements rather than their internal content if that content is not exposed in the DOM
        - For dynamic content (lists, grids, cards), use the actual container classes or structural patterns from the React components
        - When multiple elements have similar content, use unique attributes, hierarchy, or position-based selectors to target the correct one

        ### Content Verification Guidelines:
        - When verifying filtered results, DO NOT assume that category information is displayed in product cards unless explicitly shown in the React component code
        - Focus on verifiable changes like:
          * Page headings that update to reflect the filter
          * Product counts that change
          * Presence/absence of products rather than their internal category labels
          * URL changes or other state indicators
        - If the React component does not render category information in the product card, do not try to find it in the DOM
        - Always check what data is actually rendered by examining the React component structure

        ### Output:
        - Return the complete `{step_path}` file with all steps implemented, using only selectors and UI flows that are verifiable from the provided code.
        - Ensure the generated code works with shared browser session managed by environment.py.

        ### Related Source Code:
        {data_code}

        ### Existing Step File:
        {step_code}

        ### Output:
        Return the complete `{step_path}` file with all steps implemented.
    """
    
    completion = client.chat.completions.create(
        model="gpt-4.1-mini",
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
    parser.add_argument("--end", type=int, default=3, help="End user story number (e.g., 36 for us-036)")
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