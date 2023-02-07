s = input()
a = s[:s.find('h') + 1]
b = s[s.find('h') + 1 :s.rfind('h')]
c = s[s.rfind('h'):]
print(a + b.replace('h', 'H') + c)