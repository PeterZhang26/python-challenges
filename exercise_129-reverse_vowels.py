# Write a function called reverse_vowels. This function should reverse the vowels in a string. Any characters
# which are not vowels should remain in their original position. You should not consider "y" to be a vowel.

"""
reverse_vowels("Hello!") # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
"""
s = "Hello!"
print(len(s) - 1)
print(len(s))


def reverse_vowels(s):
    # Initialize list of vowels
    vowels = "aeiou"
    string = list(s)  # Convert the string passed into function into list
    i, j = (
        0,
        len(s) - 1,
    )  # Used for 2 for loops to traverse string, python indexing starts at 0

    while i < j:
        if string[i].lower() not in vowels:
            i += 1  # If character is not a vowel, move to the right
        elif string[j].lower() not in vowels:
            j -= 1  # If character is not a vowel, move to the left
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
    return "".join(string)


print(reverse_vowels("Hello!"))  # "Holle!"
print(reverse_vowels("Tomatoes"))  # "Temotaos"
print(reverse_vowels("Reverse Vowels In A String"))  # "RivArsI Vewols en e Streng"
print(reverse_vowels("aeiou"))  # "uoiea"
print(reverse_vowels("why try, shy fly?"))  # "why try, shy fly?"
