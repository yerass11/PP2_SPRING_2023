#5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re 

file = open("/Users/erasyl/Desktop/PP2_SPRING_2023/practise/regexx/tx.txt", "r")

result = re.findall(r".*a.*b$", file.read())
print(result)