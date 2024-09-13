######################################
### Directory content to text file ###
######################################
### Author: Florian Wohlkinger     ###
### Date: 13.09.2024               ###
### Version: 1.0.0                 ###
######################################

### Features
# - Traverse through directories and subdirectories to capture all file names and extensions
# - Count the number of files in each folder and display it
# - Option to save the results to a text file with a suggested or user-defined filename
# - Basic error handling for invalid folder paths


import os
import datetime


def directory_to_text(folder_path):
    """
    This function captures the filenames and file extensions of all files in a directory,
    including subdirectories, and returns the content as a list. It also provides a summary
    of how many files each folder contains and the total number of files.

    Parameters:
    - folder_path (str): The path to the directory whose contents need to be captured.

    Returns:
    - file_content (list): A list of strings containing the directory structure information.
    """

    total_file_count = 0  # Variable to keep track of the total number of files
    file_content = []  # List to store the text content for printing later

    # Walk through the directory and subdirectories
    for root, subdirs, files in os.walk(folder_path):
        file_count = len(files)  # Count the number of files in the current folder
        total_file_count += file_count  # Add to the total file count

        # Store folder-specific information
        file_content.append(f"\nFolder: {root}\n")

        # Write file names as they appear in file explorer
        for filename in files:
            file_content.append(f"  {filename}\n")

        # Store the number of files in the folder at the end
        file_content.append(f"Number of files in this folder: {file_count}\n")

    # Store the total file count summary at the end
    file_content.append(f"\nTotal number of files: {total_file_count}\n")

    return file_content


# Error handling for folder path input
try:
    folder_path = input("Please enter the full path of the folder: ")

    # Check if the path exists and is a directory
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder '{folder_path}' not found.")
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"'{folder_path}' is not a directory.")
except Exception as e:
    print(f"Error: {e}")
    exit(1)

# Capture the directory contents
file_content = directory_to_text(folder_path)

# Print the directory contents to the console for review
print("\nDirectory contents:\n")
print(''.join(file_content))

# Ask the user if they want to save the results to a text file
save_choice = input("Would you like to save the results to a text file? (y/n): ").strip().lower()

if save_choice == 'y':
    # Generate a default output filename based on the folder name and current date
    folder_name = os.path.basename(os.path.normpath(folder_path))
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    suggested_filename = f"{folder_name}_contents_{current_time}"

    # Display the suggested filename
    print(f"\nSuggested output file name: '{suggested_filename}.txt'")

    # Ask the user to manually enter a file name or accept the suggested one
    output_file = input("Enter an alternative filename (or press Enter to accept the suggestion): ").strip()

    # Use the suggested filename if the user presses Enter
    if not output_file:
        output_file = f"{suggested_filename}.txt"
    else:
        # Ensure the user includes ".txt" extension if they provide an alternative filename
        if not output_file.endswith('.txt'):
            output_file += '.txt'

    try:
        # Write the content to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(file_content)
        print(f"\nDirectory contents saved to: {output_file}")
    except Exception as e:
        print(f"Error saving file: {e}")
else:
    print("\nResults not saved.")