# Write a function called sum_pairs which accepts a list and a number and returns the first pair of numbers that sum to the number passed to the function.

"""
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
"""


def sum_pairs(my_list, val):
    for i in my_list:
        for j in my_list:
            if i + j == val and i is not j:
                return [i, j]

    return []


print(sum_pairs([3, 8, 1, 23, 48, 91], 99))


"""
Given the list and value, function needs to loop through and check the sum of 2 numbers
in the list. For example, in the list [3,8,1,23,48,91] and value 99, the function needs
to loop through each pair of numbers together until it finds a pair where the sum of the
two numbers equals to 99
"""
