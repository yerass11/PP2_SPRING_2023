word = 'Fooball, volleyball, SKAte'
words = word.split(', ')
for i in range(len(words)):
    words[i] = words[i].capitalize()
result = ' and '.join(words)

print(result)