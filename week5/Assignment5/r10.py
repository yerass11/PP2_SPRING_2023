import re
file = open("/Users/erasyl/Desktop/PP2_SPRING_2023/week5/Assignment5/tx.txt", "r")

s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', file.read())
result = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
print(result)
