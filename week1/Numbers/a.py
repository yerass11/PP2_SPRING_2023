"""
There are three numeric types in Python:

*int
*float
*complex

Variables of numeric types are created when you assign a value to them:
"""
#Example
x = 1    # int
print(type(x))
#* Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

y = 2.8  # float
print(type(y))
#* Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
#* Float can also be scientific numbers with an "e" to indicate the power of 10.

z = 1j   # complex
print(type(z))
#* Complex numbers are written with a "j" as the imaginary part:

#You can convert from one type to another with the int(), float(), and complex() methods:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))