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
