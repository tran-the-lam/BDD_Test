from openai import OpenAI
from dotenv import load_dotenv
import os
import argparse


# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI()

def generate_bdd_from_user_story(user_story, code):
    us_prompt = f"Based on the following user story and Python code, write a .features file, only file content without explanation:\n\nUser Story:\n{user_story}\n\nPython Code:\n{code}"
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
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument("--us_path", type=str, help="The user story path to generate BDD scenarios")
    parser.add_argument("--code_path", type=str, help="The code path to generate BDD scenarios")
    parser.add_argument("--prefix_output", type=str, help="The prefix of the feature file")

    # Parse the arguments
    args = parser.parse_args()


    with open(f"{args.us_path}", 'r') as file:
        # user_stories = file.read().splitlines()
        user_stories = file.read()
        
    with open(f"{args.code_path}", "r") as f:
        code = f.read()
    
    bdd_scenarios = generate_bdd_from_user_story(user_stories, code)
        
    # Clear data
    bdd_scenarios = bdd_scenarios.replace("```gherkin", "")
    bdd_scenarios = bdd_scenarios.replace("```", "")
    print(f"Generated BDD Scenarios: {bdd_scenarios}")
    
    # Save the generated BDD scenarios to a file 
    # feature_filename = f"features/{args.prefix_output}_{user_stories.index(user_story) + 1}.feature"
    feature_filename = f"features/{args.prefix_output}.feature"
    with open(feature_filename, 'w') as feature_file:
        feature_file.write(bdd_scenarios)
            
    # for user_story in user_stories:
    #     print("------------------------------------------------")
        
        
        # break
        