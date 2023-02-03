
#Python Loops
# todo Python has two primitive loop commands:

#* while loops
#* for loops

#* The while Loop:


#* With the while loop we can execute a set of statements as long as a condition is true.

#Print i as long as i is less than 6:

i = 1
while i < 6:
    print(i)
    i += 1
#The while loop requires relevant variables to be ready, 
# in this example we need to define an indexing variable, i, which we set to 1.


#Exit the loop when i is 13:
i = 10
while i < 16:
    print(i)
    if i == 13:
        break
    i += 1



#Continue to the next iteration if i is 3:

i = 0
while i < 6:
    i += 1 
    if i == 3:
        continue
    print(i)
    
    
    
#Print a message once the condition is false:

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")