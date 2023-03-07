s = input()
def palindrome_string(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]
print(palindrome_string(s))