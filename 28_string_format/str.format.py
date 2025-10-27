# str.format() = optional method that gives users
#                more control when displaying output

animal = "cow"
item = "moon"

# print("The "+animal+" jumped over the "+item) # not a good way to do it
# print("The {} jumped over the {}".format("cow","moon")) # better way to do it
# print("The {} jumped over the {}".format(animal,item)) # better way to do it

# print("The {1} jumped over the {0}".format(animal,item)) # posttional argument


# print("The {man} jumped over the {thing}".format(man="jay",thing="river")) # keyword argument


# text = "The {} jumped over the {}"

# print(text.format(animal,item)) # better way to do it