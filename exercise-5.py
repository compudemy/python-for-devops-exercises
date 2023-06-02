import shutil

def backup_directory(source_directory, destination_directory):
    # Copy all files and directories from source to destination
    shutil.copytree(source_directory, destination_directory)


# Test the function with sample source and destination directories
source_directory_path = "/path/to/source_directory"  # Replace with the path to your source directory
destination_directory_path = "/path/to/destination_directory"  # Replace with the path to your destination directory

backup_directory(source_directory_path, destination_directory_path)
