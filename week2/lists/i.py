#List Comprehension
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

#Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []


for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
#With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
print(newlist)


#The Syntax
#newlist = [expression for item in iterable if condition == True]
#The return value is a new list, leaving the old list unchanged.

##Condition
#The condition is like a filter that only accepts the items that valuate to True.

#Only accept items that are not "apple":

newlist = [x for x in fruits if x != "apple"]

#The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

#The condition is optional and can be omitted:

#With no if statement:

newlist = [x for x in fruits]

#Iterable
#The iterable can be any iterable object, like a list, tuple, set etc.

#You can use the range() function to create an iterable:

newlist = [x for x in range(10)]

#Same example, but with a condition:

#Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]

#Expression
#The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:


#Set the values in the new list to upper case:

newlist = [x.upper() for x in fruits]

#You can set the outcome to whatever you like:


#Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits]

#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:


#Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]

#The expression in the example above says:

#"Return the item if it is not banana, if it is banana return orange".