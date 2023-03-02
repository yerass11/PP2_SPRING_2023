"""
## Python Math library

1. Write a Python program to convert degree to radian.
```
Input degree: 15
Output radian: 0.261904
```
"""

pi = 22/7
degrees = float(input("Input degrees ==> "))

radians = degrees * pi / 180
print(radians)

"""
2. Write a Python program to calculate the area of a trapezoid.
```
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
```
"""
h = int(input())
a = int(input())
b = int(input())
S = h * (a + b) / 2
print(S)
"""
3. Write a Python program to calculate the area of regular polygon.
```
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
```
"""
from math import tan, pi
n_sides = int(input("Input number of sides: "))
s_length = float(input("Input the length of a side: "))
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print("The area of the polygon is: ",p_area)

"""
4. Write a Python program to calculate the area of a parallelogram. 
```
Length of base: 5
Height of parallelogram: 6
Expected Output: 30.0
```
"""
l = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))
s = l * h
print(s)