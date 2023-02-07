s = input()
f_word = s[:s.find(' ')] 
s_word = s[s.find(' ') + 1:]
print(s_word + ' ' + f_word)