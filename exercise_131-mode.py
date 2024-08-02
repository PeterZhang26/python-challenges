# Write a function called mode. This function accepts a list of numbers and returns the
# most frequent number in the list of numbers. You can assume that the mode will be unique.


def mode(nums):
    # Create empty frequency dictionary
    frequency = {}

    # For loop goes through each number in the list to count occurrences
    for num in nums:
        if num in frequency:
            frequency[
                num
            ] += 1  # If the number is already in the dictionary, increment its count
        else:
            frequency[num] = (
                1  # If the number is not in the dictionary, add it with a count of 1
            )

    # Findind the most frequently occuring number
    max_count = 0
    mode_number = None

    # Loop goes through the frequency dictionary to find the number with the highest count
    for num, count in frequency.items():
        if count > max_count:
            max_count = count  # Update max_count with the higher count
            mode_number = num  # Update mode_number with the corresponding number

    print(frequency)
    return mode_number  # Return the number with the highest count


print(mode([2, 4, 1, 2, 3, 3, 4, 4, 5, 4, 4, 6, 4, 6, 7, 4]))

"""
We want to count the number that occurs the most given a defined list with numbers
populated. What we need to do here is assign a count to each number and store that
count to each individual number, which we can achieve by using a dictionary. The key
value pair of the dictionary will be the number and the count of the number. After
The empty dictionary frequency is first initiated, then we loop through the list of
numbers, with an if condition. If the number already exists in the dictionary, add
a counter +1, else if the number is not in the dictionary already then set the count 
to 1. Once the dictionary is created, we set 2 variables. Max count = 0 and mode_number
= None. The next for loop is dictionary iteration, for the numbers and counts of numbers
in the dictionary items, if the count value is > max_count then set max_count to that
value, then update mode_number to the corresponding number with the max_count. Once
the number with the biggest count is found, return the number key paired with that
value.
"""
