import os

def list_files_and_directories(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print("File:", file_path)
        
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            print("Directory:", dir_path)


# Test the function with a sample directory
directory_path = "/path/to/directory"  # Replace with the path to your directory
list_files_and_directories(directory_path)
