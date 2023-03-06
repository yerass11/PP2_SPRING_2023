import re
file = open("/Users/erasyl/Desktop/PP2_SPRING_2023/week5/Assignment5/tx.txt", "r")

result = re.sub(r'(?:_+)(\w)', lambda m: m.group(1).upper(), file.read())
print(result)



