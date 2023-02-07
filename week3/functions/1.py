def my_function():
    print("Hello from a function")

my_function()

def my_function(fname):
    print(fname + " Omar")

my_function("Alua")
my_function("Almas")
my_function("Shyngys")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


def my_function(*family):
    print("Members of Cheboley are " + family[2])

my_function("Jin", "Kim", "O")

def my_function(child1, child2, child3):
    print("The youngest one is " + child1)
my_function(child1 = "Alua", child2 = "Arma", child3 = "Arnur")

def func(**disc):
    print("Now we study disciplines like" + disc["math"])
func(math = "Statistics", gum = "Global")

def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def func_of_list(food):
    for x in food:
        print(x)
food = ["bread", "banana", "yoghurt"]
func_of_list(food)

def func_return(x):
    return 5 * x
print(func_return(3))
print(func_return(5))

def emptyfunc():
    pass

#recursion

def recforsub(k):
    if(k > 0):
        result = k + recforsub(k - 1)
        print(result)
    else:
        result = 0
        return result
print("Recursion Example Results")
recforsub(10)




