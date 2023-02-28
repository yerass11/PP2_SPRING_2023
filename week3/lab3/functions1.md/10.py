def unique(list):
    newlist = []
    for x in thislist:
        if x not in newlist:
            newlist.append(x)
    print(newlist)
thislist = [int(x) for x in input().split()]
unique(list)