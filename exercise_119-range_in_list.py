"""
range_in_list

Write a function called range_in_list which accepts a list and start and end indices, and 
returns the sum of the values between (and including) the start and end index.

If a start parameter is not passed in, it should default to zero. If an end parameter is 
not passed in, it should default to the last value in the list. Also, if the end argument 
is too large, the sum should still go through the end of the list.
"""

"""
range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0
"""


def range_in_list(list1, start=0, end=None):
    end = end or list1[-1]
    return sum(list1[start : end + 1])


"""
This function is returning the sum of values in the list provided, with 2 parameters set.
A start parameter and an end parameter, default values are provided for the parameters if
they aren't set when calling the function. The end parameter is either set to None or it
is set to the end of the list index which is list1[-1]. Return is just slicing through the
list provided with the parameters set, and then summing each number of the list within the
range.
"""

print(range_in_list([1, 3, 2, 4, 24, 5, 2, 12, 2, 3], 0, 5))
print()
print(
    f"This is the sum of your numbers provided from start to end: {range_in_list([1, 3, 2, 4, 24, 5, 2, 12, 2, 3], 0, 5)}"
)
