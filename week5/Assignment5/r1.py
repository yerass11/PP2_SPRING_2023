import re

file = open("/Users/erasyl/Desktop/PP2_SPRING_2023/week5/Assignment5/tx.txt", "r")

result = re.findall(".*a.*b.*", file.read())
print(result)