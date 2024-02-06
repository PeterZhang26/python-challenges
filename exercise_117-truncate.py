"""
Write a function called truncate that will shorten a string to a specified length, and add "..." to the end.  
Given a string and a number n, truncate the string to a shorter string containing at most n characters. 
For example, truncate("long string", 5)  should return a 5 character truncated version of "long string".  
If the string gets truncated, the truncated return string should have a "..." at the end. Because of this, 
the smallest number passed in as a second argument should be 3. 
"""

"""
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
"""


def truncate(string, num):
    if num < 3:
        return "Truncation must be at least 3 characters."
    else:
        if len(string) > 3 and len(string) > num:
            return string[: (num - 3)] + "..."
        else:
            return string


print(truncate("We are the champions of the world!", 12))

"""
This function is truncating the last 3 letters of the string/word with '...', given 2 input parameters,
string being the actual string passed to the function specified, and num being the number of characters
that should be returned. The string 'Hello World' has 11 indexes including the blank space, if passed
num = 6 then 6 characters need to be returned by the function, with the last 3 characters being '...'.
The function uses list slicing to determine the range of characters returned as [:num - 3], meaning the
range is [:3] with the addition of '...' that will return 'Hel...'
"""
