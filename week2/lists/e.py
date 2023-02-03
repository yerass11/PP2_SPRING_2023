#Change the second item:
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1] = "blackcurrant"
print(thislist)



#Change a Range of Item Values
#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist)
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)



#Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1:3] = ["watermelon"]
print(thislist)



#Insert Items
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.insert(2, "watermelon")
print(thislist)