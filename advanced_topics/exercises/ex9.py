def nth(l, n):
    if n >= 0:
        print(l[n])
    else:
        print(l[n + len(l)])


nth(['a', 'b', 'c', 'd'], -2)
