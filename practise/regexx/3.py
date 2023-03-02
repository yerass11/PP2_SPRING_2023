#3. Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

file = open("/Users/erasyl/Desktop/PP2_SPRING_2023/practise/regexx/tx.txt", "r")

result = re.findall("[a-z]+_[a-z]+", file.read())
print(result)