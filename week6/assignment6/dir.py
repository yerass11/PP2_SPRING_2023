#1###############################################################
import os
path = 'c:\\py\\pyForgit\\'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])
# #2##############################################################
print('Exist:', os.access('c:\\py\\pyForgit', os.F_OK))
print('Readable:', os.access('c:\\py\\pyForgit', os.R_OK))
print('Writable:', os.access('c:\\py\\pyForgit', os.W_OK))
print('Executable:', os.access('c:\\py\\pyForgit', os.X_OK))
#3##################################################################
print("Test a path exists or not:")
path = r'c:\\py\\pyForgit'
print(os.path.exists(path))
path = r'c:\\py\\pyForgit'
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))
# 4############################################################################
def file(name):
    with open(name) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


print("Number of lines in the file: ", file("s.txt"))
#5############################################################################
color = ["colum", "word", "number"]
with open('s.txt', "w") as fr:
        for i in color:
                fr.write("%s\n" % i)
content = open('s.txt')
print(content.read())
#6###############################################################################
import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)
#7##############################################################################
from shutil import copyfile
copyfile('s.py', 'ss.py')
#8####################################################################
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")