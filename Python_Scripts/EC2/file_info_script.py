import os

# Get the current working directory
cwd = os.getcwd()

# Get a list of files in the working directory
files = os.listdir(cwd)

# Create an empty list to store file information
dict_list = []

# Iterate over each file in the directory
for file_name in files:
    # Get the full path of the file
    file_path = os.path.join(cwd, file_name)
    
    # Get the file size in bytes
    file_size = os.path.getsize(file_path)
    
    # Get the file creation time
    creation_time = os.path.getctime(file_path)
    
    # Get the file modification time
    modification_time = os.path.getmtime(file_path)
    
    # Create a dictionary with file information
    file_info = {
        'file_name': file_name,
        'file_path': file_path,
        'file_size': file_size,
        'creation_time': creation_time,
        'modification_time': modification_time
    }
    
    # Add the file information to the list
    dict_list.append(file_info)

# Print each file dictionary on a new line
for file_info in dict_list:
    print(file_info)
    print()