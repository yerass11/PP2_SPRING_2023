#2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
file = open("/Users/erasyl/Desktop/PP2_SPRING_2023/practise/regexx/tx.txt", "r")

result = re.findall(r".*a.*b.*b.*|.*a.*b.*b.*b.*", file.read())

print(result)