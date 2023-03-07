s = input()
cnt1 = 0
cnt2 = 0
for c in s:
    if c >= 'A' and c <= 'Z':
        cnt1 += 1
    if c >= 'a' and c <= 'z':
        cnt2 += 1

print(cnt1)
print(cnt2)