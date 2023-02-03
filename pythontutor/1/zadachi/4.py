n = int(input())

h = n // 60 - ((n // 60) // 24) * 24
m = n % 60

print (h, m)
