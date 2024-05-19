import re

def print_welcome_message():
    """Display the welcome message to the user."""
    message = """
    -------------------------------------------------
    Welcome to the CV Generator!
    -------------------------------------------------

    This program helps you create your professional CV easily from the command line.

    To use the CV Generator:
    1. Follow the prompts to provide information for each section of your CV.
    2. Once you've entered all the necessary details, your completed CV will be displayed.
    3. Your completed CV will also be saved to a file named cv_output.txt in the current directory.

    Let's get started! Please provide the requested information when prompted.
    """
    print(message)

def read_template(template_path):
    """Reads a template file and returns its content as a string"""
    try:
        with open(template_path, "r") as file:
            return file.read()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Template file not found at the specified path: {template_path}") from e

def parse_template(template_string):
    """Extract placeholders from the template."""
    pattern = r'\{([^}]+)\}'
    matches = re.findall(pattern, template_string)
    stripped_template = re.sub(pattern, '{}', template_string)
    return stripped_template, tuple(matches)

def prompt_user_for_input(template_parts):
    """Prompt the user for input based on placeholders."""
    return {part: input(f"Enter your {part}: ") for part in template_parts}

def merge(template, values):
    """Merge values into a template string."""
    return template.format(*values)

def main():
    """Main function to run the CV generator."""
    print_welcome_message()
    
    # Use a relative path for the template file
    template_path = "../assest/cv_template.txt"  
    template_content = read_template(template_path)
    
    # Parse the template to get placeholders
    stripped_template, template_parts = parse_template(template_content)
    
    # Get user input for each placeholder
    user_input = prompt_user_for_input(template_parts)
    
    # Merge the input values into the template
    filled_template = merge(stripped_template, tuple(user_input.values()))
    
    print("Your completed CV:")
    print(filled_template)

    # Save the filled template to a file
    output_file_path = "cv_output.txt"
    with open(output_file_path, "w") as output_file:
        output_file.write(filled_template)

if __name__ == "__main__":
    main()
