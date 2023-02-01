a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == c and b == d-1:
    print("YES")
elif a == c and b == d+1:
    print("YES")
elif a == c+1 and b == d-1:
    print("YES")
elif a == c+1 and b == d+1:
    print("YES")
elif a == c-1 and b == d-1:
    print("YES")
elif a == c-1 and b == d+1:
    print("YES")
elif a == c-1 and b == d:
    print("YES")
elif a ==c+1 and b == d:
    print("YES")
else:
    print("NO")