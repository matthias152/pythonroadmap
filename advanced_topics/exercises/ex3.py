def remove_every_other(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    print(new_list)


remove_every_other([3, 5, 2, 5, 1, 1])
