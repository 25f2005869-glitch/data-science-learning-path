# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Dictionaries
# Day         : 10
# Description : Understanding dictionary creation,
#               access, update and traversal.
# ==========================================================

# Creating a dictionary
student = {
    "name": "Saloni",
    "age": 20,
    "course": "PDSA"
}

print("Dictionary:", student)

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

# Adding a new item
student["city"] = "Prayagraj"

# Updating a value
student["age"] = 21

print("Updated Dictionary:", student)

# Removing an item
student.pop("course")

print("After Removal:", student)

# Dictionary traversal
print("Dictionary Items:")

for key, value in student.items():
    print(key, ":", value)