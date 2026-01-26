dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figure"]
}

print(dictionary)

subjects = {
    "python", "java", "c++", "python", "javascript", "java", 
    "python", "java", "c++", "c"
}

print(subjects)

subjects = {
    "python", "java", "c++", "python", "javascript", "java", 
    "python", "java", "c++", "c"
}

print(len(subjects))

marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

print(marks)

values = {9, 9.0}
print(values)

values = {9, 9.25}
print(values)

values = {9, "9.0"}
print(values)

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)

#print(hello)
#print(hello)
#print(hello)
#print(hello)
#print(hello) if we don't want to repat this so we use loop

#whileTrue :
     #print(hello)
     #it is wrong way to write the code because we create an 
     #infinite loop by writing this.

count = 1
while count <= 5 :
    print("hello")
    count += 1     