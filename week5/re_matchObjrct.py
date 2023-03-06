import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object


#The Match object has properties and methods used to retrieve information about the search, and the result:

#.span() returns a tuple containing the start-, and end positions of the match.
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


#.string returns the string passed into the function
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


#.group() returns the part of the string where there was a match
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())


# If there is no match, the value None will be returned, instead of the Match Object.