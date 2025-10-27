import time

# epoch = a date and the time from which your computer measures system time

# print(time.ctime(1000000))     # ctime method will conver a time expressed in seconds since epoch to a readable string
#                                # epoch = when your computer thinks time began
# the 1000000 in the above function means that the system will take the time past the 1000000 secs from the epoch time


# print(time.time())          # return current seconds since epoch

# print(time.ctime(time.time()))      # returns the current time

time_object = time.localtime()
# time_object = time.gmtime()     # directly gives the utc time

# local_time = time.strftime("%B %d %Y %H:%M:%S",time_object) # output = October 26 2025 12:35:41
# print(local_time)

# time_string = "20 April, 2020"
# time_object = time.strptime(time_string, "%d %B, %Y")
# print(time_object)


# (year , month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple) # asctime converts the tuple to a string of a time
# time_string = time.mktime(time_tuple) # takes a tuple representaion of time or a time object and converts it into seconds from the epoch date 
print(time_string)



