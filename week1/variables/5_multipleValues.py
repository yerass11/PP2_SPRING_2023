#Python allows you to assign values to multiple variables in one line:

#Example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


#And you can assign the same value to multiple variables in one line:
#Example
x = y = z = "Orange"
print(x)
print(y)
print(z)


#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

#Example
#Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)