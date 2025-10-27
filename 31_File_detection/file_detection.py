import os


path = "/Users/ishan/Documents/file_detection/folder"

# path = "/Users/ishan/Documents/file_detection/file.txt" this is for checking the file


if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory/folder")
else:
    print("That location doesn't exist!")