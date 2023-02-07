string = input()
half = len(string)//2 + len(string)%2
print(string[half:] + string[:half])