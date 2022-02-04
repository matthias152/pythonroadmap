'''
intersection(['a', 'b', 'z'], ['x', 'y'. 'z']) returns ['z']
'''


def intersection(list1, list2):
    in_common = []
    for i in list1:
        if i in list2:
            in_common.append(i)
    return in_common
