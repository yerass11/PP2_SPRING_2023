i = 1
while i != 0:
    a = int(input())
    if a == 0:
        break
    if a < 10:
        continue
    elif a > 100:
        break
    else:
        print(a)   