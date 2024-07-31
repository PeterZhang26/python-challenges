# Create a function running_average that returns a function. When
# the function returned is passed a value, the function returns the
# current average of all previous function calls. You will have to
# use closure to solve this. You should round all answers to the
# 2nd decimal place.

"""
rAvg = running_average()
rAvg(10) # 10.0
rAvg(11) # 10.5
rAvg(12) # 11

rAvg2 = running_average()
rAvg2(1) # 1
rAvg2(3) # 2
"""


def running_average():
    # Start with empty sum and count variables
    total_sum = 0
    count = 0

    # Inner function that calculates the running average
    def average(new_average):
        # Declare total_sum and count as nonlocal to modify them in this scope
        nonlocal total_sum, count
        # Update the total sum with the new value
        total_sum += new_average
        # Increment the count of numbers used for the function
        count += 1
        # Calculate the running average and round it to 2 decimal places
        return round(total_sum / count, 2)

    # Return the inner function to be called externally with new value
    return average


rAvg = running_average()
print(rAvg(10))  # 10.0
print(rAvg(11))  # 10.5
print(rAvg(12))  # 11
