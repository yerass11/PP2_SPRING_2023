n = int(input())
k = n // 2
l = r = k
for i in range(k + 1):
    for j in range(n):
        if l < 0:
            break
        if (l == j or r == j):
            print("*", end = "")
        else: 
            print(" ", end = "")
    l -= 1
    r += 1
    print()

l += 2
r -= 2

for i in range(k + 1):
    for j in range(n):
        if l > k:
            break
        if (l == j or r == j):
            print("*", end = "")
        else: 
            print(" ", end = "")
    l += 1
    r -= 1
    print()
    