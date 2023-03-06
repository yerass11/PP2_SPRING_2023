#6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re 

file = open("/Users/erasyl/Desktop/PP2_SPRING_2023/practise/regexx/tx.txt", "r")

result = re.sub("[ ,.]", ":", file.read())
print(result)