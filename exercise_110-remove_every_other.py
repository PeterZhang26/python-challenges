# Write a function called remove_every_other that accepts a list and returns a new list with every second value removed.

"""
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
"""


def remove_every_other(my_list):
    return [val for index, val in enumerate(my_list) if index % 2 == 0]


""" 
The list has values and indexes in the list, so by using list comprehension 
and enumerate. We only include values where the index divided by 2 is equal 
to 0. Example list [6,73,4,2,9] has indexes of 0,1,2,3,4. 0/2 = 0, 1/2 != 0
and so forth. That means the new list is [6,4,9]
"""

remove_every_other([6, 73, 4, 2, 9])
