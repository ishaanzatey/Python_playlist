# thread = a flow if execution. Like a separate order of instructions.
#          However each thread takes a turn running to achieve concurrency
#          GIL = (global interpreter lock),
#          allows only one thread to hold the control of the python interpreter at any one time

# cpu bound = program/task spends most of its time waiting for internal events (CPU intensive) 
#             use multiprocessing

# io bound = program/task spends most of its time waiting for external events (user input, web scrapping) 
#            use multithreading

import threading
import time


def eat_breakfast():
    # print("You are eating breakfast")
    time.sleep(3)
    print("You ate breakfast")

def drink_coffee():
    # print("You are drining coffee")
    time.sleep(4)
    print("You drank coffee")

def study():
    # print("You are studing")
    time.sleep(5)
    print("You finish studying")

# eat_breakfast()
# drink_coffee()
# study()

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()


# if we use the join the main threads need to wait till the x y and z threads completed its executes and joins after finishing the tasks
x.join()
y.join()
z.join()


print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())      
# the main thread does not perform the actions in the functions of the code but does create the multiple threads based on the requirement which we have mentioned