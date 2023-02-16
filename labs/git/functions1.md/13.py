from random import randint
print("Hello! What is your name?")
name = str(input())
print("Well, " + name + ", I am thinking of a number between 1 and 20.")
print("Take a guess.")
a = randint(0, 20)
cnt = 0
n = int(input())
f = 1

while f <= 20:
    cnt += 1
    if n < a:
        print("Your guess is too low.")
        print("Take a guess.")
    elif n > a:
        print("Your guess is too high.")
        print("Take a guess.")
    elif a == n:
        print("Good job, " + name + "! You guessed my number in" , cnt , "guesses!")
        break    
    n = int(input())