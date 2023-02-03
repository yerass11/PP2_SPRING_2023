a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a+b == c+d or abs(a-c) == abs(d-b) or a == c or b == d:
    print("YES")
else:
    print("NO")