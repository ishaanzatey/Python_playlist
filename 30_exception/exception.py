# exception = events detected during execution that interrupt the flow of a program

import re
from unittest import result

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator

except ZeroDivisionError as e:
    print("You can't divide by zero! idiot")
    print(e)

except ValueError as e:
    print("Enter only numbers please")
    print(e)

except Exception as e:
    print("Something went wrong :(")
    print(e)

else:
    print(result)

finally:
    print("This will always execute")