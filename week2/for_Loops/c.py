
#*The range() Function
##To loop through a set of code a specified number of times, we can use the range() function,
##The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.


#*Using the range() function:

for x in range(6):
    print(x)

#*Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

#The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):


#Using the start parameter:

for x in range(2, 6):
    print(x)

#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):


#Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
    print(x)

#Else in For Loop
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:


#Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
    print(x)
else:
    print("Finally finished!")

#*Note: The else block will NOT be executed if the loop is stopped by a break statement.


#Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

#Nested Loops
#A nested loop is a loop inside a loop.

#The "inner loop" will be executed one time for each iteration of the "outer loop":


#Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

#The pass Statement
#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.


for x in [0, 1, 2]:
    pass