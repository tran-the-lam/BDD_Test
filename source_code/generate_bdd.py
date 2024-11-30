from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI()

def generate_bdd_from_user_story(user_story, login_code):
    us_prompt = f"Based on the following user story and Python code, write a .features file, only file content without explanation:\n\nUser Story:\n{user_story}\n\nPython Code:\n{login_code}"
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a Quality Analyst."},
            {
                "role": "user",
                "content": us_prompt
            }
        ]
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    with open('user-story.txt', 'r') as file:
        user_stories = file.read().splitlines()
        
    with open("login.py", "r") as f:
        login_code = f.read()
    
    for user_story in user_stories:
        print("------------------------------------------------")
        print(f"User Story: {user_story}")
        bdd_scenarios = generate_bdd_from_user_story(user_story, login_code)
        ### clear data
        bdd_scenarios = bdd_scenarios.replace("```gherkin", "")
        bdd_scenarios = bdd_scenarios.replace("```", "")
        print(f"Generated BDD Scenarios: {bdd_scenarios}")
        
        # Save the generated BDD scenarios to a file 
        feature_filename = f"features/user_story_{user_stories.index(user_story) + 1}.feature"
        with open(feature_filename, 'w') as feature_file:
            feature_file.write(bdd_scenarios)
        
        break
        