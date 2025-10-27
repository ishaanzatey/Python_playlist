# text = 'Hello\nMy name is ishan\nthis file is written by me'
text_append = "\nI have later appened this below text\nHow are you"
last_append_read = "\nBye see yaa!\nGood night"

# with open('write_in_this','w') as file:
# with open('write_in_this','a') as file:
#     file.write(text_append)

with open('write_in_this', 'a+') as file: # a is for append and a+ is to append and read
    file.write(last_append_read)
    file.seek(0)          # Move cursor to start of file to read the file
    print(file.read())  # only prints the new line and not the entire content of the file
    # content = file.read()
    # print(content)
    