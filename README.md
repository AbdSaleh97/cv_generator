# CV Generator

The CV Generator is a command-line program designed to assist users in creating their professional CVs quickly and easily.

## Overview

The program operates by following these simple steps:

1. **Welcome Message**: Upon execution, the program greets the user and provides an overview of its functionality.
2. **Read Template**: It reads a template file containing placeholders for various sections of the CV.
3. **Parse Template**: The template is parsed to identify placeholders.
4. **Prompt for Input**: Users are prompted to input information for each section of the CV.
5. **Merge**: The input values are merged into the template to create the completed CV.
6. **Display and Save**: The completed CV is displayed to the user and saved to a file named `cv_output.txt` in the current directory.

## How to Use

To use the CV Generator:

1. **Clone the Repository**: Clone or download the repository to your local machine.
2. **Install Python**: Ensure you have Python installed on your system.
3. **Navigate to Directory**: Using the command line, navigate to the directory where the `cv_generator.py` file is located.
4. **Run the Program**: Execute the program by running the following command:
5. **Follow Prompts**: Follow the prompts to provide information for each section of your CV.
6. **View Output**: Once all information is provided, the completed CV will be displayed on the screen.
7. **Access Saved CV**: Additionally, a file named `cv_output.txt` will be created in the current directory containing the completed CV.

## File Structure

- `cv_generator.py`: The main Python script containing the CV generation logic.
- `assets/`: Directory containing supporting files.
- `cv_template.txt`: Template file for the CV.
