def allPermut():
    s = input().split()
    for i in range(len(s)):
        for j in range(len(s)-1):
            print(*s)
            s[j], s[j+1] = s[j+1], s[j]