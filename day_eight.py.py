marks = 74

if(marks >= 90):
    grade = "A"
elif(marks >=80 and marks <90):
     grade = "B"
elif(marks >=70 and marks <80):
     grade = "C"
else:
     grade = "D"
print("grade of the student -->", grade)

marks = input("enter student marks : ")

if(marks >= 90):
    grade = "A"
elif(marks >=80 and marks <90):
     grade = "B"
elif(marks >=70 and marks <80):
     grade = "C"
else:
     grade = "D"
print("grade of the student -->", grade)

marks = int(input("enter student marks : "))

if(marks >= 90):
    grade = "A"
elif(marks >=80 and marks <90):
     grade = "B"
elif(marks >=70 and marks <80):
     grade = "C"
else:
     grade = "D"
print("grade of the student -->", grade)

age = 34

if(age >= 18):
     if(age >= 80):
          print("cannot drive")
     else:
       print("can drive")
else:
     print("cannot drive")


age = 95

if(age >= 18):
     if(age >= 80):
          print("cannot vote")
     else:
       print("can vote")
else:
     print("cannot vote")