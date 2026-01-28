nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx", i)
        break
    else:
        print("finding..")
    i += 1 

i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1

print("end of loop")

i = 0
while i <= 5:
     if(i == 3):
         i += 1
         continue
     print(i)
     i += 1

i = 0
while i <= 10:
     if(i%2 == 0):
         i += 1
         continue
     print(i)
     i += 1

i = 0
while i <= 10:
     if(i%2 != 0):
         i += 1
         continue
     print(i)
     i += 1

nums = [1, 2, 3, 4, 5]

for val in nums:
    print(val)

veggies = ["potato", "tomato", "cabbage","onion"]

for val in veggies:
    print(val)

str = "apnacollege"

for char in str:
    print(char)  

str = "apnacollege"

for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)
else:
    print("END") 

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in nums:
    print(el)

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 49

idx = 0
for el in nums:
    if(el == x):
        print("number found at idx", idx)
        
        idx += 1

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 49

idx = 0
for el in nums:
    if(el == x):
        print("number found at idx", idx)
        break
    idx += 1

    


     