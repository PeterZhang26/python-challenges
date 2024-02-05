"""
Write a function called includes which accepts a collection, a value, and an optional starting index. 
The function should return True if the value exists in the collection when we search starting from the 
starting index. Otherwise, it should return False.

The collection can be a string, a list, or a dictionary. If the collection is a string or array, the 
third parameter is a starting index for where to search from. If the collection is a dictionary, the 
function searches for the value among values in the dictionary; since objects have no sort order, the 
third parameter is ignored.
"""

"""
includes([1, 2, 3], 1) # True 
includes([1, 2, 3], 1, 2) # False 
includes({ 'a': 1, 'b': 2 }, 1) # True 
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
"""


def includes(
    collection, value, start=0
):  # function defintion requires 3 arguments, the collection, a value and the starting index
    # check condition if collection of values is string or list
    if type(collection) == str or type(collection) == list:
        collection = collection[start:]

        if value in collection:
            return True

    # seperate condition in else statement for dictionary collection values
    else:
        if value in collection.values():
            return True

    return False


"""
This function is trickier to understand, the definition itself requires 3 arguments, which
is a collection of values, a single value and then a starting index for the collection
specified. The if type(collection) first checks for the type of data being read, either
a str or list type. If it is True, then collection searches using list slicing, with the
starting index as the parameter and end of the list as the end. If the value passed in the
argument does exist in the collection of values then it returns True. After, the else 
statement is checking for if the value, not the key exists in the dictionary key and value 
pairs, which returns True if it does exist
"""
