classmates = ["Aarav", "Priya", "Rahul", "Sneha", "Dev"]
print("Class list: " , classmates)
print("Total students: ", len(classmates))
print("First student: ", classmates[0])
print("Last student: ", classmates[-1])
print("First three: ", classmates[:3])
classmates.append("Meera")
print("\nAfter adding Meera: ", classmates)
classmates.remove("Dev")
print("After removing Dev: ", classmates)
classmates.sort()
print("Sorted alphabetically", classmates)
classmates.reverse()
print("Reversed: ", classmates)
teacher = {"name": "Mr Sharma", "subject": "Python", "experience": 5}
print("\nTeacher profile:", teacher)
print("Subject: ", teacher["subject"])
print("Experience: ", teacher.get("experience", "Not found"))
teacher["experience"] = 6
teacher["email"] = "sharma@school.com"
teacher.pop("Updated teacher profile: ", teacher)
