#In Python, the data type is set when you assign a value to a variable:

a = "Hello World"	#str
print(type(a))

b = 20	#int
print(type(b))

c = 20.5	#float
print(type(c))

d = 1j	#complex
print(type(d))


e = ["apple", "banana", "cherry"]	#list
print(type(e))

f = ("apple", "banana", "cherry")	#tuple
print(type(f))

g = range(6)	#range
print(type(g))

h = {"name" : "John", "age" : 36}	#dict
print(type(h))

i = {"apple", "banana", "cherry"}	#set
print(type(i))

j = frozenset({"apple", "banana", "cherry"})	#frozenset
print(type(j))

k = True	#bool
print(type(k))

l = b"Hello"	#bytes
print(type(l))

m = bytearray(5)	#bytearray
print(type(m))

n = memoryview(bytes(5))	#memoryview
print(type(n))

o = None	#NoneType
print(type(o))
