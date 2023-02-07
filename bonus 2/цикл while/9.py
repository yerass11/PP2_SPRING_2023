max = 0
len = 0
max_index = 0
element = int(input())
while element !=0:
    if element > max:
        max = element
        max_index = len
    len +=1
    element = int(input())
print(max_index)