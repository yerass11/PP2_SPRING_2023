import re

txt = "The rain in Spain"
x = re.findall("\w+ai\w+$", txt)
print(x)



txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)