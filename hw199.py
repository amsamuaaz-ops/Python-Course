student_data = {
    "id1": {"name": "Sara", "class": "V", "subject": "english, math, science"},
    "id2": {"name": "David", "class": "V", "subject": "english, math, science"},
    "id3": {"name": "Sara", "class": "V", "subject": "english, math, science"},
    "id4": {"name": "Surya", "class": "V", "subject": "english, coding, math"}
}
print(student_data)
print(student_data.get("id1", "Not found"))

print(student_data.get("id5", "Not found"))

student_data["id5"] = {
    "name" : "vikash", 
    "class":"V", 
    "subject": "english,coding,math"
}
student_data["id2"]["subject"] = "english,science,coding"

cleaned_data = {}
seen_records = []

for i, details in student_data.items():
    unique_key = (details["name"],details["class"],details["subject"])
    if unique_key not in seen_records:
        seen_records.append(unique_key)
        cleaned_data[i] = details
removed_student =  student_data.pop("id4","student not found")
print("The student who removed")
print(removed_student)
print("The students left are",len(student_data))

for i, details in student_data.items():
    print(i,":",details)
    