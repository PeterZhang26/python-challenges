"""
Write a function called two_list_dictionary which accepts two lists of varying lengths.The first list consists of
keys and the second one consists of values. Your function should return a dictionary created from the keys and 
values. If there are not enough values, the remaining keys should have a value of null. If there not enough keys,
just ignore the remaining values.
"""

"""
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}
"""


def two_list_dictionary(list1, list2):
    print(f"Length of list 1: {len(list1)}")
    print(f"Length of list 2: {len(list2)}")
    if len(list1) > len(list2):
        print(f"        list1 - list2 length: {len(list1)-len(list2)}")
        for i in range(len(list1) - len(list2)):
            list2.append(None)
        return dict(zip(list1, list2))

    return dict(zip(list1, list2))


print(two_list_dictionary(["a", "b", "c", "d"], [1, 2, 3]))
