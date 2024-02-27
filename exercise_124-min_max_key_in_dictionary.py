"""
min_max_key_in_dictionary

Write a function called min_max_key_in_dictionary which returns a list with 
the lowest key in the dictionary and the highest key in the dictionary. You 
can assume that the dictionary will have keys that are numbers.
"""

"""
min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}) # [1,4]
"""


def min_max_key_in_dictionary(my_dict):
    keys = my_dict.keys()

    print(keys)
    return [min(keys), max(keys)]


print(min_max_key_in_dictionary({2: "a", 7: "b", 1: "c", 10: "d", 4: "e"}))  # [1,10])

"""
We want a function that takes a dictionary as an input, with already set keys
and values. The function should return the minimum and maximum keys, N.B the
keys, not the values associated with the keys. We can use min and max functions
as well as assigning the keys of the dictionary to a variable with keys = my_dict.keys()
"""
