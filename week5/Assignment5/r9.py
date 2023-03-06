import re
file = open("/Users/erasyl/Desktop/PP2_SPRING_2023/week5/Assignment5/tx.txt", "r")

result = re.sub(r"(\w)([A-Z])", r"\1 \2", file.read())
print(result)
