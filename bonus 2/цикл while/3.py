n = int(input())
i = 0
while 2**i <= n:
    i += 1
print(i-1, 2**(i-1))