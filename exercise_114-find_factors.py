# Write a function called find_factors which accepts a number and returns a list of all of the numbers which are is divisible by starting from 1 and going up to the number.

"""
find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
find_factors(111) # [1,3,37,111 ]
find_factors(321421) # [1,293,1097,321421 ]
find_factors(412146) # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]
"""


def find_factors(number):
    return [i for i in range(1, number + 1) if number % i == 0]


print(find_factors(42069))
print(find_factors(80))


"""
The function is essentially finding all the factors that the input number has,
which means even numbers will have more factors due to the nature of mathematics
and multiplication. The factors need to return a remainder of 0 when iterating
through the potential factor, if it has a remainder of 0 then it is a factor.
All numbers are divisible by 1 and the value of the number itself, so the function
needs a range starting from 1 up until the number itself + 1, because the range
function is not inclusive of the end.
"""
