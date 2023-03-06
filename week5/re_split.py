import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)