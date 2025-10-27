# higher order function = a function that either 
                            # 1. takes one or more functions as arguments
                            # 2. returns a function as its result
#                             (In Python, functions are also treated as objects)

# # Example of the 1st case

# def loud(text):
#     return text.upper()

# def quiet(text):
#     return text.lower()

# def hello(func):
#     text  = func("Hello")
#     print(text)

# hello(loud)
# hello(quiet)



# Example of the 2nd case

def divisor(x):
    def dividned(y):
        return y/x
    return dividned


divide = divisor(2)
print(divide(10))