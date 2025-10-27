import os


# path = 'text.txt'
# # os.remove('text.txt')

# try:
#     os.remove(path)
# except FileNotFoundError:
#     print("That file was not found")



# TO DELETE EMPTY FOLDER

# path_dir = "empty_folder"
# # os.remove('text.txt')

# try:
#     os.rmdir(path_dir) #  Directory not empty: 'empty_folder' error if there is file in the folder
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to delete that")
# else:
#     print(path_dir + " was deleted")





# TO DELETE FOLDER WITH FILES

import shutil

path_dir = "folder_with_file"
os.rmdir

try:
    # os.rmdir(path_dir) # throws OSError Exception
    shutil.rmtree(path_dir) #  removes the entire directory and the files inside the directory
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path_dir + " was deleted")