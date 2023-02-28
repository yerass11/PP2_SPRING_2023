import json
print("------------------")
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))

print("__________________")


#The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
#The json.dumps() method has parameters to make it easier to read the result:
print(json.dumps(x, indent=4))

print("__________________")
#You can also define the separators, default value is (", ", ": "), 
# #which means using a comma and a space to separate each object,
# #and a colon and a space to separate keys from values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

print("__________________")
#The json.dumps() method has parameters to order the keys in the result:
print(json.dumps(x, indent=4, sort_keys=True))