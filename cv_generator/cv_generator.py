import re

def print_welcome_message():
    print("-------------------------------------------------")
    print("Welcome to the CV Generator!")
    print("-------------------------------------------------")
    print()
    print("This program helps you create your professional CV easily from the command line.")
    print()
    print("To use the CV Generator:")
    print("1. Follow the prompts to provide information for each section of your CV.")
    print("2. Once you've entered all the necessary details, your completed CV will be displayed.")
    print("3. Your completed CV will also be saved to a file named cv_output.txt in the current directory.")
    print()
    print("Let's get started! Please provide the requested information when prompted.")

def read_template(template_path):
    """Reads a template file and returns its content as a string"""
    try:
        with open(template_path, "r") as file:
            template_content = file.read()
        return template_content
    except FileNotFoundError:
        raise FileNotFoundError(f"Template file not found at the specified path: {template_path}")




def parse_template(template_string):
    pattern = r'\{([^}]+)\}'
    matches = re.findall(pattern, template_string)
    stripped_template = re.sub(pattern, '{}', template_string)
    return stripped_template, tuple(matches)

def prompt_user_for_input(template_parts):
    user_input = {}
    for part in template_parts:
        user_input[part] = input(f"Enter your {part}: ")
    return user_input

def merge(template, values):
    """
    Merge values into a template string.
    """
    return template.format(*values)

def main():
    print_welcome_message()
    template_path = "../assest/cv_template.txt"  
    template_content = read_template(template_path)
    stripped_template, template_parts = parse_template(template_content)
    user_input = prompt_user_for_input(template_parts)
    filled_template = merge(stripped_template, tuple(user_input.values()))
    print("Your completed CV:")
    print(filled_template)


    output_file_path = "cv_output.txt"
    with open(output_file_path, "w") as output_file:
        output_file.write(filled_template)

if __name__ == "__main__":
    main()
