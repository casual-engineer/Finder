import os

def search_files_and_folders(root_dir, search_string):
    # Iterate through all directories and files in the root directory
    for root, dirs, files in os.walk(root_dir):
        for folder in dirs:
            if search_string in folder:
                folder_path = os.path.join(root, folder)
                print("Folder: " + folder_path)
        
        for file in files:
            if search_string in file:
                file_path = os.path.join(root, file)
                print("File: " + file_path)

search = str(input('search: '))
search_files_and_folders('C:\\', search)
print('Finished searching!')
while True:
    None

