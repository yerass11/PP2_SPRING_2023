#Use the len method to print the length of the string.
x = "Hello World"
print(len(x))


#Get the first character of the string txt.
txt = "Hello World"
x = txt[0]
print(x)


#Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
x = txt[2:5]
print(x)


#Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()
print(x)


#Convert the value of txt to upper case.
txt = "Hello World"
txt = txt.upper()
#Convert the value of txt to lower case.
txt = txt.lower()


#Replace the character H with a J.
txt = "Hello World"
txt = txt.replace("H", "J")


#nsert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))