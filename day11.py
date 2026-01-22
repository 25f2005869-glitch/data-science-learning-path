tup = (2, 1, 3, 1)
print(type(tup))

tup = (2, 1, 3, 1)
print(tup[0])
print(tup[1])

tup = ()
print(tup)
print(type(tup))

tup = (1, )
print(tup)
print(type(tup))

tup = (1)
print(tup)
print(type(tup))

tup = (1.0) 
print(tup)
print(type(tup))

tup = ("hello") 
print(tup)
print(type(tup))

tup = (1, 2, 3, 4) 
print(tup)
print(type(tup))

tup = (1, 2, 3, 4) 
print(tup[1:3])

tup = (1, 2, 3, 4) 
print(tup.index(2))

tup = (1, 2, 3, 4, 2, 2) 
print(tup.count(2))

movies = []
mov1 = input("enter 1st movie: ")
mov2 = input("enter 2nd movie: ")
mov3 = input("enter 3rd movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

movies = []
mov1 = input("enter 1st movie: ")
mov2 = input("enter 2nd movie: ")
mov3 = input("enter 3rd movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

movies = []
mov = input("enter 1st movie: ")
movies.append(mov)
mov = input("enter 2nd movie: ")
movies.append(mov)
mov = input("enter 3rd movie: ")
movies.append(mov)

print(movies)

movies = []
movies.append(input("enter 1st movie: "))
movies.append(input("enter 2nd movie: "))
movies.append(input("enter 3rd movie: "))

print(movies)

list1 = [1, 2, 1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

list1 = [1, 2, 3]


copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome") 

list1 = ["m", "a", "a", "m"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

list1 = ["m", "a", "a", "m", "p"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)


