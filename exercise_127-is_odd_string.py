"""
is_odd_string

Write a function called is_odd_string which returns true if sum of each character's
position in the alphabet is odd. For example, "a" is in the first position, "b" is 
in the second position, and so on. If the sum is even, return false.  NOTE: INDEXING 
STARTS AT 1.  A is position 1, NOT POSITION 0.
"""

"""
is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
"""
import string


def is_odd_string(st):
    # Directly set alphabets variable as lowercase ascii letters
    alphabets = string.ascii_lowercase
    total = 0
    for char in st.lower():
        # Check if the character is a lowercase letter
        if char in alphabets:
            # Shifting the index up by 1 to account for indexing starting at 1
            total += alphabets.index(char) + 1
    # Checking if the sum of the alphabets is odd
    return total % 2 != 0


print(is_odd_string("veryfun"))  # True

"""
This function is an exercise on list indexing, given that indexing in python starts
at 0, so there is a need to shift the index up by one. We know that the conventional
alphabet starts at 1 for a and ends at 26 for z. So we need to loop through the given
string passed into the function and then sum all the positional values of the letters
and check whether the final sum divided by 2 has a remainder of 0 or not. If it has a
remainder of 0, then the sum is even and the function returns False. If the sum is odd,
then the function returns True.

"""
