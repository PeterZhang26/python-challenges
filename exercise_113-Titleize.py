# Write a function called titleize which accepts a string of words and returns a new string with the first letter of every word in the string capitalized.

"""
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
"""


def titleize(sentence):
    return " ".join(word[0].upper() + word[1:] for word in sentence.split(" "))


print(titleize("I'm a SUPERSTAR defying the laws of GRAVITY!"))

"""
The input of this function is a string that could have capital letters already,
knowing string methods where you can have an empty string use the .join method
on the space. The method would be to join the empty string, while using a for
looop to iterate through each word in the sentence passed. The function has 2
parts, where the first part is to capitalize the first letter of the word by
using list slicing to get index[0], then after that to join the capital letter
with the rest of the word through list slicing to get index[1:] which is index
1 until the end of the word. The word is then joined to the empty string at the
start of the function.
"""
