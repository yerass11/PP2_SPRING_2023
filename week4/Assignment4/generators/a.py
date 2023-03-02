"""

## Python iterators and generators

1. Create a generator that generates the squares of numbers up to some number `N`.

2. Write a program using generator to print the even numbers between 0 and `n` in comma separated form where `n` is input from console.

3. Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and `n`.

4. Implement a generator called `squares` to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

5. Implement a generator that returns all numbers from (n) down to 0.

"""
#1. Create a generator that generates the squares of numbers up to some number `N`.
n = int(input())
def gensquares(n):
    for i in range(n+1): 
        if (i**2 > n):
            break
        yield i**2
#gensquares(n)
for i in gensquares(n):
    print(i)
    
    
#2. Write a program using generator 
# to print the even numbers between 0 and `n` in comma separated form where `n` is input from console.
n = int(input())
def evenNumb(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i 
for i in evenNumb(n):
    print(i)

#3.
#Define a function with a generator which can iterate the numbers, 
# which are divisible by 3 and 4, between a given range 0 and `n`.
n = int(input())
def div_3_4(n):
    for i in range(n+1):
        if (i % 3 == 0 and i % 4 == 0):
            yield i
for i in div_3_4(n):
    print(i)



#4.
#Implement a generator called `squares` to yield the square of all numbers from (a) to (b). 
# Test it with a "for" loop and print each of the yielded values.
a = int(input())
b = int(input())
def squarez(a, b):
    for i in range(a, b+1):
        yield i ** 2
for i in squarez(a, b):
    print(i)



#5.
#Implement a generator that returns all numbers from (n) down to 0.
n = int(input())
def decreas(n):
    for i in range(n, -1, -1):
        yield i
for i in decreas(n):
    print(i)