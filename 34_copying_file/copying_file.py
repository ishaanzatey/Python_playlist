# copyfile() =  copies content of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file’s creation and modification times)

import shutil

shutil.copyfile('text.txt','copy.txt')  #src , destination
shutil.copy('text.txt','copy2.txt')  #src , destination
shutil.copy2('text.txt','copy3.txt')  #src , destination

#shutil.copyfile('/Users/ishan/Documents/BroCode/34_copying_file/text.txt', '/Users/ishan/Desktop/copy.txt')  #src , destination by giving paths