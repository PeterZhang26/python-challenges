"""
sum_up_diagonals

Write a function called sum_up_diagonals which accepts an NxN list of lists 
and sums the two main diagonals in the array: the one from the upper left 
to the lower right, and the one from the upper right to the lower left.
"""

"""
EXAMPLES:


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
sum_up_diagonals(list1) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
sum_up_diagonals(list2) # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

sum_up_diagonals(list3) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
sum_up_diagonals(list4) # 68
"""


def sum_up_diagonals(arr):
    sum = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                sum = sum + arr[i][j]
            if (i + j) == (len(arr) - 1):
                sum = sum + arr[i][j]
    return sum


"""
Double for loop function that loops through the list of arrays with i, then the list
of elements in the ith array with a j for loop. If i == j then the element is the
diagonal element of the array itself, the first if statement checks for the condition,
the second if statement is checking the reverse diagonal condition. For the first
element of the reverse diagonal, len(arr) - 1 = 3, which means i + j must == 3 in
order to include the correct element to sum, if i = 0 and j = 3 then arr[0][3] = 4
is the correct element to add to the sum of the diagonal for the reverse direction
"""

list4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

print(len(list4))

sum_up_diagonals(list4)  # 68
