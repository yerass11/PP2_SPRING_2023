#In the loop, when i is 3, jump directly to the next iteration.

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)