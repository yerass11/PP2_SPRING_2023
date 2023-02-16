first_integer = int(input())
operator = input()
second_integer = int(input())
if operator == '+':
    result = first_integer + second_integer
    print(result)
if operator == '-':
    result = first_integer - second_integer
    print(result)
if operator == '/':
    result = first_integer // second_integer
    print(result)
if operator == '*':
    result = first_integer * second_integer
    print(result)