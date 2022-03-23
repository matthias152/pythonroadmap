def find_duplicate(arr):
    arr2 = []
    check = 0
    length = len(arr)
    # print(length)
    for i in arr:
        if i not in arr2:
            arr2.append(i)
            check = check + 1
            # print(check)
            if check == (length):
                print("No duplicates")
        elif i in arr2:
            print(i)
            break


find_duplicate([2, 1, 4, 3, 12])
