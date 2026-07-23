student_grades = {
                   "Ahmed" : 9,
                   "Muaaz" : 8,
                   "Ahad": 5,
                   "Zain": 10,
                   "Aysha": 8
}

class_total = 40
total_students = 5
average = 0





   

print(max(student_grades))


print(min(student_grades))

name = input("whose grade do want to check")
if name == "Muaaz":
    print(student_grades.get("Muaaz"))
elif name == "Ahmed":
   print(student_grades.get("Ahmed"))
elif name == "Ahad":
    print(student_grades.get("Ahad"))
elif name == "Zain":
    print(student_grades.get("Zain"))
elif name == "Ayesha":
    print(student_grades.get("Ayesha"))
else:
    "There's no name"