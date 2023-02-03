#Loop through the items in the fruits list.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x) 




#In the loop, when the item value is "banana", jump directly to the next item.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)



#Use the range function to loop through a code set 6 times.

for x in range(6):
    print(x)
    
    
    
    
    
    
#Exit the loop when x is "banana".


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)