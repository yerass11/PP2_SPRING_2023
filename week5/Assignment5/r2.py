import re
file = open("/Users/erasyl/Desktop/PP2_SPRING_2023/week5/Assignment5/tx.txt", "r")

result = re.findall(r".*a.*b.*b.*|.*a.*b.*b.*b.*", file.read())

print(result)