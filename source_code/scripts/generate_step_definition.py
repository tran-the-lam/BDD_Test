import os
import re
import argparse

def generate_step_definitions(feature_file, step_file):
    """
    Generate step definitions from a .feature file and write them to a steps file.
    """
    print(f"Generating '{step_file}' from '{feature_file}'")
    if not os.path.exists(feature_file):
        print(f"Feature file '{feature_file}' not found.")
        return

    # Regular expression to match Gherkin steps
    step_pattern = re.compile(r'^\s*(Given|When|Then|And)\s+(.*)')

    # Read the feature file
    with open(feature_file, 'r') as f:
        lines = f.readlines()

    # Prepare the step definitions
    step_definitions = []
    previous_step_type = None
    for line in lines:
        match = step_pattern.match(line)
        if match:
            step_type = match.group(1)  # Given, When, Then, And
            step_text = match.group(2).strip()  # The step text

            # Handle "And" by using the previous step type
            if step_type == "And":
                step_type = previous_step_type

            # Escape quotes in the step text
            step_text_escaped = step_text.replace('"', '\\"')

            # Generate the step definition function
            step_definitions.append(f"""
@{step_type.lower()}('{step_text}')
def step_impl(context):
    # TODO: Implement step: {step_text}
    raise NotImplementedError(\""" Step not implemented: {step_text} \""")
""")
            previous_step_type = step_type  # Update the previous step type

    with open(step_file, 'w') as f:
        f.write("from behave import given, when, then\n")
        f.write("\n".join(step_definitions))

    print(f"Step definitions written to '{step_file}'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Add arguments
    # parser.add_argument("--prefix_feature", type=str, help="The prefix of the feature file")
    # parser.add_argument("--code_path", type=str, help="The code path to generate steps")
    parser.add_argument("--task", type=str, help="The task to perform")
    args = parser.parse_args()
    
    file = f"features/{args.task}.feature"
    step_file = f"features/steps/steps_{args.task}.py"
        
    generate_step_definitions(file, step_file)