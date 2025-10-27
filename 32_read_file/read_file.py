# with open('file.txt') as file:
# # with open('/Users/ishan/Documents/BroCode/32_read_file/file.txt') as file: # this also works
#     print(file.read())

# print(file.closed) # file is closed outside the with block


# seeing exception

try:
    with open('file.txt') as file: # this also works
        print(file.read())
    
except FileNotFoundError:
    print('File was not found')