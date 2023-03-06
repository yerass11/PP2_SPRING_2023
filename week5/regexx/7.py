# 7.Write a python program to convert snake case string to camel case string.
import re

file = open("/Users/erasyl/Desktop/PP2_SPRING_2023/practise/regexx/tx.txt", "r")

result = re.sub("[_]", "", file.read())
result = re.sub("(.*?)_([a-zA-Z])", file.read())
print(result)