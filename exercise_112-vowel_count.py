# Write a function called vowel_count that accepts a string and returns a dictionary with the keys as the vowels and values as the count of times that vowel appears in the string.

"""
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
"""


def vowel_count(word):
    new_dict = {}
    for vowel in word.lower():
        if vowel in "aeiou":
            new_dict[vowel] = word.lower().count(vowel)

    dict_keys = list(new_dict.keys())

    dict_keys.sort()
    sorted_dict = {i: new_dict[i] for i in dict_keys}

    return new_dict, sorted_dict


print(vowel_count("Superstitious"))

"""
The main aim is to iterate through the given string and then map the every vowel
that appears in the given string to the dictionary in a key:value pair, the for
loop iterates through the string (also lowercase of the string). If statement
checks if the string character is in the list of vowels given. If it is then the
dictionary is assigned the count of the number of times the vowel appears as the
value for the key. Added functionality as well of sorting the vowels alphabetically.
"""
