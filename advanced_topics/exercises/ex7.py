def find_factors(num):
    new_list = []
    i = 1
    while(i <= num):
        if (num % i == 0):
            new_list.append(i)
        i += 1
    print(new_list)


find_factors(10)
