a = int(input())
b = int(input())
for i in range(a + a%2 - 1, b - 1, -2):
    print(i)
    