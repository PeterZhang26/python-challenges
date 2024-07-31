# Write a function called three_odd_numbers, which accepts a list of numbers
# and returns True  if any three consecutive numbers sum to an odd number.

"""
three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
"""


def three_odd_numbers(nums):
    # For loop to loop through a list, need 3 consecutive number elements
    for i in range(len(nums) - 2):  # Looking for i, i+1 and i+2
        # Check if the sum of the three numbers is odd
        sum_of_three = nums[i] + nums[i + 1] + nums[i + 2]
        # Check if the sum is odd
        if sum_of_three % 2 != 0:
            return True

    # If no odd sum is found, return False
    return False


print(three_odd_numbers([1, 2, 3, 4, 5]))  # True
print(three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0]))  # True)
