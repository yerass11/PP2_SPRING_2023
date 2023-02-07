max = 0
n = int(input())
count = 0
mylist = []
while n != 0 :
    if n > max:
        max = n
    mylist.append(n)
    n = int(input())
for i in range(len(mylist)):
    if mylist[i] == max:
        count += 1
print(count)