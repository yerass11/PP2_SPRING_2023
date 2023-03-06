#4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re

file = open("/Users/erasyl/Desktop/PP2_SPRING_2023/practise/regexx/tx.txt", "r")

result = re.findall("[A-Z]{1}[a-z]+", file.read())
print(result)