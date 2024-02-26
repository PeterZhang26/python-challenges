"""
nth

Write a function called nth, which accepts a list and a number and returns the element at
whatever index is the number in the list. If the number is negative, the nth element from 
the end is returned.

You can assume that number will always be between the negative value of the list length, 
and the list length minus 1.
"""

"""
nth(['a', 'b', 'c', 'd'], 1)  # 'b' 
nth(['a', 'b', 'c', 'd'], -2) #  'c'
nth(['a', 'b', 'c', 'd'], 0)  # 'a'
nth(['a', 'b', 'c', 'd'], -4) #  'a'
nth(['a', 'b', 'c', 'd'], -1) #  'd'
nth(['a', 'b', 'c', 'd'], 3)  # 'd'
"""


def nth(list1, num):
    return list1[num]


my_list = [1, 3, 4, 5, 44, 888, 12, 4]

print(nth(my_list, 5))

"""
This function is returning the value at which the index of the list is input, Python
indexing starts at 0 so for the first element of a list you would call the function
to have nth(my_list, 0).
"""
