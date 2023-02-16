def palindrom(s):
    return s[::-1] == s
s = str(input())
if palindrom(s):
    print("Palindrome")
else:
    print("Not Palindrome")