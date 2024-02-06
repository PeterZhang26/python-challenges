"""
Write a function called repeat, which accepts a string and a number and returns a new string with the string 
passed to the function repeated the number amount of times. Do not use the built in repeat method!
"""

"""
repeat('*', 3) # '***' 
repeat('abc', 2) # 'abcabc' 
repeat('abc', 0) # ''
"""


def repeat(string, num):
    if num == 0:
        return ""
    return string * num


print(repeat("rockstar", 3))
print(repeat("empty", 0))
