#Sort List Alphanumerically
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

#Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana", 'banan']
print(thislist)
thislist.sort()
print(thislist)

print("--------")

#Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort()
print(thislist)

print("--------")

#To sort descending, use the keyword argument reverse = True:
#Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(thislist)
thislist.sort(reverse = True)
print(thislist)

print("--------")

#Sort the list descending:

thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort(reverse = True)
print(thislist)

print("--------1")

#Customize Sort Function
#You can also customize your own function by using the keyword argument key = function.

#The function will return a number that will be used to sort the list (the lowest number first):

#Sort the list based on how close the number is to 50:

def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

print("--------2")

#Case Insensitive Sort
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:


#Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist)
thislist.sort()
print(thislist)

print("--------3")

#Luckily we can use built-in functions as key functions when sorting a list.

#So if you want a case-insensitive sort function, use str.lower as a key function:


#Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist)
thislist.sort(key = str.lower)
print(thislist)

print("--------4")

#Reverse Order
#What if you want to reverse the order of a list, regardless of the alphabet?

#The reverse() method reverses the current sorting order of the elements.


#Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist)
thislist.reverse()
print(thislist)

print("--------")