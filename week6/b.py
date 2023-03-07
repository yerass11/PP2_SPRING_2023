import csv

students = []

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name":row[0], "home":row[1]})
        
for student in sorted(students, key=lambda student: student["name"], reverse=False):
    print(f"{student['name']} is from {student['home']}")