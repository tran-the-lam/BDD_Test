from openai import OpenAI
from dotenv import load_dotenv
import os
import argparse

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def generate_bdd_from_user_story(user_story):
    data_code = ""
    for k, v in map_file_to_content.items():
        data_code += f"##### {k}:\n{v}\n\n"
        
    us_prompt = f"""
        Based on the following user story and source code, write a .features file, only file content without explanation:\n\n
        User Story:\n{user_story}\n\n
        Source Code:\n{data_code}"""
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a Quality Analyst."},
            {"role": "user", "content": us_prompt},
        ],
    )

    return completion.choices[0].message.content

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

    us_path = f"user-stories/{args.task}.txt"
    with open(us_path, "r") as file:
        user_stories = file.read()

    read_all_file_in_folder(args.folder)
    
    bdd_scenarios = generate_bdd_from_user_story(user_stories)

    # Preprocess data before saving
    bdd_scenarios = bdd_scenarios.replace("```gherkin", "")
    bdd_scenarios = bdd_scenarios.replace("```", "")

    # Save the generated BDD scenarios to a file
    feature_filename = f"features/{args.task}.feature"
    with open(feature_filename, "w") as feature_file:
        feature_file.write(bdd_scenarios)
