s = input()
s1 = ''
for i in range(len(s)):
    if i % 3 != 0:
        s1 = s1 + s[i]
        
print(s1)