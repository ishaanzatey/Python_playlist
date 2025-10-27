# reduce() = apply a function to an iterable and reduce it to a single cumulative value
#              performs function on first two elements and repetes process until 1 value remains

# reduce(function, iterable)  
import functools


# letters = ["H", "E" , "L", "L", "O"]
# word = functools.reduce(lambda x,y : x + y, letters)
# print(word)



# we can use it for the factorial of a number

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y: x * y , factorial)    # how this works is 5(x)*4(y) = 20(becomes x) then 20(x)*3(y) = 60(becomes x) then 60*2 = 120 then 120*1 = 120
print(result)