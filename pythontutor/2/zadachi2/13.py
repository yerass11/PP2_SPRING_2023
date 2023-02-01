N=int(input())
M=int(input())
x=int(input())
y=int(input())

if N<M:
    if M-y<y and N-x<x:
        if M-y<N-x:
            print(M-y)
        else:
            print(N-x)
    elif M-y<y and N-x>x:
        if M-y<x:
            print(M-y)
        else:
            print(x)
    elif M-y>y and N-x>x:
        if x<y:
            print(x)
        else:
            print(y)
    elif M-y>y and N-x<x:
        if N-x<y:
            print(N-x)
        else:
            print(y)
elif M<N:
    if N-y<y and M-x<x:
        if N-y<M-x:
            print(N-y)
        else:
            print(M-x)
    elif N-y<y and M-x>x:
        if N-y<x:
            print(N-y)
        else:
            print(x)
    elif N-y>y and M-x>x:
        if x<y:
            print(x)
        else:
            print(y)
    elif N-y>y and M-x<x:
        if M-x<y:
            print(M-x)
        else:
            print(y)
