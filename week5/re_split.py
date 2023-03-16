import re

txt = "The rain in Spain"
x = re.split("ai", txt)
print(x)


txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)