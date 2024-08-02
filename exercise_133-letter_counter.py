# Write a function called letter_counter which accepts a string and returns a function. When
# the inner function is invoked it should accept a parameter which is a letter, and the inner
# function should return the number of times that letter appears. This inner function should
# be case insensitive.

"""
counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1 
"""


def letter_counter(string):
    # Convert the string to lowercase to make it case-insensitive
    lower_string = string.lower()

    # Inner function that does actual count of letter
    def count_letter(letter):
        # Convert the letter to lowercase
        lower_letter = letter.lower()
        # Count occurrences of the letter in the string, input parameter is letter chosen
        return lower_string.count(lower_letter)

    return count_letter


counter = letter_counter("Amazing")
print(counter("a"))  # 2
print(counter("m"))  # 1

counter2 = letter_counter("This Is Really Fun!")
print(counter2("i"))  # 2
print(counter2("t"))  # 1

counter3 = letter_counter("Look at all the audacious applicable words I applaud about")
print(counter3("a"))  # 9
