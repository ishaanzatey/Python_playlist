# daemon thread = a thread that runs in the background, not important for program to run 
#                 your program will not wait for daemon thread to complete before exiting
# non-daemon threads cannot normally be killer, stay alive until task is complete

#                 ex. background tasks, garbage collection, waiting for input, long running process

import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ", count, "seconds")


x = threading.Thread(target=timer, daemon=True)
x.start()

# we can also change the thread to a daemon thread or non daemon thread
# but we can change it during the execution


answer = input("Do you want to exit?")