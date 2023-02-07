count = 0
pre = int(input())
while pre!=0:
    element = int(input())
    if element > pre and pre != 0:
        count += 1
    pre = element
print(count)