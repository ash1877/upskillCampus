
#Program:

import os
from pathlib import Path

# A list with associated  file extension
list_of_directories = {
    "Picture_Folder": [".jpeg", ".jpg", ".gif", ".png"],
    "Video_Folder": [".wmv", ".mov", ".mp4", ".mpg", ".mpeg", ".mkv"],
    "Zip_Folder": [".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".zip"],
    "Music_Folder": [".mp3", ".msv", ".wav", ".wma"],
    "PDF_Folder": [".pdf"],
}

#  dictionary mapping file extensions to their respective directory names 

file_format_dictionary = {
    final_file_format: directory
    for directory, file_formats in list_of_directories.items()
    for final_file_format in file_formats
}

# Define the organizer function

def organizer():
    current_path = Path('.')

    # Iterate through all files and directories in the current directory
    for entry in os.scandir():
        if entry.is_dir():
            continue  # Skip directories
        
        file_path = Path(entry)
        final_file_format = file_path.suffix.lower()

        #  To Check if the file extension is in the file_format_dictionary

        if final_file_format in file_format_dictionary:
            directory_name = file_format_dictionary[final_file_format]
            directory_path = current_path.joinpath(directory_name)

            # Create the directory if it doesn't exist
            os.makedirs(directory_path, exist_ok=True)

            # Move the file to the appropriate directory
            os.rename(file_path, directory_path.joinpath(file_path))

    # Create "Other_Folder" if it doesn't exist and move any remaining files there
    other_folder = current_path.joinpath('Other_Folder')
    os.makedirs(other_folder, exist_ok=True)

    for dir_entry in os.scandir():
        try:
            if dir_entry.is_file():
                os.rename(current_path / dir_entry.name, other_folder / dir_entry.name)
        except OSError as e:
            print(f"Failed to move file '{dir_entry.name}': {e}")

# Define the main entry point
if __name__ == "__main__":
    organizer()


