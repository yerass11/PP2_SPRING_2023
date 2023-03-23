f = open ("demofile.txt", "r")
print(f.readline().rstrip)
f.close()
print(f.readline().rstrip())