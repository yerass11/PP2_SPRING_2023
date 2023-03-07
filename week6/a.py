import csv

students = []

with open("students.csv") as file:
    for line in file:
        name, faculty = line.rstrip().split(',')
        students.append({'name': name, 'faculty': faculty})

def get_names(student):
    return student['name']

def get_faculty(student):
    return student['faculty']

for student in sorted(students, key=lambda x: x[name], reverse=False):
    print(f"(student['name'] is in {student['faculty']})")