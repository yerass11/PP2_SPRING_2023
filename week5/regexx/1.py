#1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

file = open("/Users/erasyl/Desktop/PP2_SPRING_2023/practise/regexx/tx.txt", "r")

result = re.findall(".*a.*b.*", file.read())
print(result)