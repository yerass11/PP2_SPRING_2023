#Append Items

#Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.append("orange")
print(thislist)


#Insert Items
#To insert a list item at a specified index, use the insert() method.

#The insert() method inserts an item at the specified index:
#Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.insert(1, "orange")
print(thislist)
# As a result of the examples above, the lists will now contain 4 items.



#Extend List
#Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
print(thislist)
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)




#Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
