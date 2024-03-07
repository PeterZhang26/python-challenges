"""
find_greater_numbers

Write a function called find_greater_numbers which accepts a list and 
returns the number of times a number is followed by a larger number 
across the entire list. 

Take the example find_greater_numbers([6,1,2,7]) # 4 , there are 4 
times where a number is followed by a greater number:  

1. 2 > 1
2. 7 > 6
3. 7 > 1
4. 7 > 2 
"""

"""
find_greater_numbers([1,2,3]) # 3 
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
"""


def find_greater_numbers(my_list):
    num_count = 0
    for index, row in enumerate(my_list):
        num_count += sum(1 for i in my_list[index:] if i > row)
    return num_count


print(find_greater_numbers([6, 1, 2, 7]))

"""
Yes, this exercise is written unclear unfortunately. It's confusing but after some re-reading it's understandable.

My description:

- Starting from the 0'th element

- iterate over the list of numbers once, but:

- for each iteration, count how many times the number of the current index is followed by a larger number until the end of the list.

[0] [1] [2] [3]

'6' '1' '2' '7'

(1) 6 is smaller than 7 = 1

(2) increment to index 1: 1 is smaller than 2 and 7 = 2

(3) increment to index 2: 2 is smaller than 7 = 1

1 + 2 + 1 = 4.
"""

"""
Including another student's explanation to help understand what the exercise is asking for. We give the function a defined list
and have a number count starting at 0, using enumerate which is a function that iterates over the list and gives you the index of
the list we loop over. If the number of the current index for it's value, is followed by a larger number in the list, add 1 to the
number count and then sum all the counts at the end of the function. In the example provided by the other student, for the list
[6,1,2,7] we have a list of length 4, starting at index [0] the value '6' is followed by one number that is bigger, '7' which adds
1 to the number count. When iterating at index [1] the value '1' is followed by two numbers '2', '7' that are bigger so add 2 to
the number count, then iterating at index [3] the value '2' is followed by one number that is bigger than '2' which is '7'. The
total count is then equal to 4.
"""
