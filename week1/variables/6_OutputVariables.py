#The Python print() function is often used to output variables.

#Example
x = "Python is awesome"
print(x)


#In the print() function, you output multiple variables, separated by a comma:

#Example
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#You can also use the + operator to output multiple variables:

#Example
x = "Python "
y = " is "
z = "awesome"
print(x + y + z)
#Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

"""
In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

Example
x = 5
y = "John"
print(x + y)
"""
#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

#Example
x = 5
y = "John"
print(x, y)