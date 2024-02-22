"""
same_frequency

Write a function called same_frequency which accepts two numbers and returns True 
if they contain the same frequency of digits. Otherwise, it returns False.
"""

"""
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
"""


def same_frequency(num1, num2):

    return sorted(str(num1)) == sorted(str(num2))


print(f"The frequency of numbers provided is {same_frequency(6942022, 4269022)}")
