# dictionary comprehension  = create dictionaries using an expression
#                             can replace for loops and certain lambda functions
# dictionary = {key : expression for (key,value) in iterable }
# dictionary = {key : expression for (key,value) in iterable if conditional }
# dictionary = {key : (if/else) expression for (key,value) in iterable }
# dictionary = {key : funcation(value) for (key,value) in iterable }

# --------------------------------------------------------------------------------------

# weather = {"New York":  "snowing", "Boston": "sunny", "Los Angeles": "sunny", "Chicago": "cloudy"}
# sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
# print(sunny_weather) # prints both key and value where value is sunny
# print(sunny_weather.keys()) # prints only keys where value is sunny



# --------------------------------------------------------------------------------------
# # Using if/else in dictionary comprehension

# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key : ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
# print(desc_cities)

# --------------------------------------------------------------------------------------
# # Using if/else in dictionary comprehension with function
def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 40 <= value < 70:
        return "WARM"
    else:
        return "COLD"


cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key : check_temp(value)  for (key,value) in cities.items()}
print(desc_cities)