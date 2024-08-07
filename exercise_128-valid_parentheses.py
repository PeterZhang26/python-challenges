"""
valid_parentheses

Write a function called valid_parentheses that takes a string of parentheses, and 
determines if the order of the parentheses is valid. valid_parentheses should return 
true if the string is valid, and false if it's invalid.
"""

"""
valid_parentheses("()") # True 
valid_parentheses(")(()))") # False 
valid_parentheses("(") # False 
valid_parentheses("(())((()())())") # True 
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
"""


def valid_parentheses(s):
    # Start with an empty list
    empty_list = []

    # Loop through each character in list
    for char in s:
        # If character is '(' append it to the list
        if char == "(":
            empty_list.append(char)

        # If character is ')' and list is not empty, remove the last element from the list
        elif char == ")":
            if empty_list:  # Check list is not empty
                empty_list.pop()  # Remove top element in list
            else:
                # If list is empty
                return False

    # After loop, check if list is empty
    return len(empty_list) == 0  # Gives true if condition met


print(valid_parentheses("(())((()())())"))  # True )
print(valid_parentheses(")(()))"))  # False )
print(valid_parentheses("(())((()())())"))  # True )
print(valid_parentheses("()()()()())()("))  # False))

"""
Working with python lists to help loop through the given string, 1st an empty
list initialized to add and remove the parentheses. First for loop iterates
the characters in the string. If condition, character is == "(" then append
to the empty list, elif condition is == ")" then remove top element from list.
Inner if statement in elif, if list is not empty pop the element, else return
False condition. The final return statment checks if the length of the list is
== 0, if the list is 0 then logic assumes there are equal number of parentheses
brackets.
"""
