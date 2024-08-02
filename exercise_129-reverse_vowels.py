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

"""
Within the function itself we first create a string variable with lowercase vowels,
then we convert the string passed into the function into a list. We initialize two 
iterators, i and j that loop from the start and the end of the string at the same time.
If the iterator i is not a vowel, we move to the right, if the iterator at j is not a
vowel we move left. We only swap the vowels when both i and j iterators are a vowel.
The iterator j starts at len(s) - 1 because of the way python indexing works, the word
"Hello!" has an index of 0 to 5, but the length of the string is 6 so we want to start
at index 5. Once the vowels are swapped, we return the an empty string with the method
.join on the string that we've swapped the vowels around.
"""
