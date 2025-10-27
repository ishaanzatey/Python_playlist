# dictionary = a changable, unordered collection of unique key-value pairs
# they are fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

# print(capitals['Germany'])  #if key does not exist, raises error
# print(capitals.get('Germany'))  #if key does not exist, returns None
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# capitals.update({'Germany':'Berlin'})  #adds key-value pair
# print(capitals.values())
# for key,value in capitals.items():
#     print(key,value)

# capitals.update({'USA':'Las Vegas'})  #updates value of key
# # print(capitals)

# for key,value in capitals.items():
#     print(key,value)

# capitals.pop('Russia')  #removes key-value pair
# print(capitals)