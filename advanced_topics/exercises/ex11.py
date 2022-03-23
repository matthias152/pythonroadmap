'''
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}
'''

def two_list_dictionary(k, v):
    diction = {}

    for i, j in enumerate(k):
        if i < len(v):
            diction[k[i]] = v[i]
        else:
            diction[k[i]] = None

    print(diction)

two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
