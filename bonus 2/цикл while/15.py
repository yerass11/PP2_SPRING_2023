a = int(input())
f1 = 1
i = f0 = fn = 0
while i < a:
    fn = f0 + f1
    f0, f1 = f1, fn
    i+=1
    if fn==a:
        print(i+1)
        break
    if fn>a or i>a:
        print(-1)
        break