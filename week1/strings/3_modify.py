#The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())
print(a.lower())


# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

# Example
#The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))
print(a)


"""
The split() method returns a list where the text between the specified separator becomes the list items.

Example
The split() method splits the string into substrings if it finds instances of the separator:
"""
a = "Python, C++, C#, SQL"
print(a.split(",")) # returns ['Hello', ' World!']