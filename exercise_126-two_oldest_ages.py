"""
two_oldest_ages

Write a function called two_oldest_ages. The function should take a list 
of numbers as its argument and return the two highest numbers within the
list. The returned value should be a list in the format [second oldest 
age, oldest age].

The order of the numbers passed in could be any order.
"""

"""
two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [6,1,9,10,4] ) # [9,10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
"""


def two_oldest_ages(my_list):
    my_list.sort()
    return my_list[-2:]


print(two_oldest_ages([1, 2, 10, 8]))  # [8, 10]

"""
Straightforward function where we want to return the two oldest ages of
a given list. The list first needs to be sorted in ascending order from
smallest to largest. After sorting the list, the last two digits need to
be sliced and returned from the function. We can slice the list by using
negative indexing[-2:], which tells the slicing to start from the end of
the list minus 2 before the end, then index until the end. 
"""
