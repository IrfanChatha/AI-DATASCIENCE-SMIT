student = {
    "name": "CLS",
    "age": "30",
    "grade": "a"
}
print("Student Dictionary : ", student)
print("Student Grade : ", student["grade"])
student["City"] = "NewYork"
print("Student City : ", student)
student["age"] = "20"
print("Student age update : ", student)
student.pop("City")
print("Student city deleted : ", student)

print(student.keys())
print(student.values())

for key, value in student.items():
    print(key, " : ", value)
