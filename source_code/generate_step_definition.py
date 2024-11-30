import os
import re

def generate_step_definitions(feature_file, steps_file):
    """
    Generate step definitions from a .feature file and write them to a steps file.
    """
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

    # Write the step definitions to the steps file
    os.makedirs(os.path.dirname(steps_file), exist_ok=True)
    with open(steps_file, 'w') as f:
        f.write("from behave import given, when, then\n")
        f.write("\n".join(step_definitions))

    print(f"Step definitions written to '{steps_file}'.")


if __name__ == "__main__":
    feature_file = "features/user_story_1.feature"  # Path to your .feature file
    steps_file = "features/steps/user_story_1.py"  # Path to the steps file to generate
    generate_step_definitions(feature_file, steps_file)