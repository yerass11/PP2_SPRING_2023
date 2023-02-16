#from itertools import product
#for i,j in product(range(1,5), range(1,5)):
#    print(i*j)

output  = []
for m in list(range(2, 11)):
    tmp = [m*z for z in list(range(2, 11))]
    output.append(tmp)

print(output)