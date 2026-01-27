count = 1
while count <= 5 :
    print("hello")
    count += 1

count = 1
while count <= 5 :
    print("hello")
    count += 1

print(count)

i = 1
while i <= 5:
    print("hello")
    i +=1

i = 1
while i <= 5:
    print("hello", i)
    i +=1

#print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

print("loop ended")

#print numbers from 1 to 5
i = 5
while i >= 1:
    print(i)
    i -= 1

print("loop ended")

#print numbers from 1 to 5
#i = 5
#while i < 6:
#  print(i)
#  i -= 1
# this gives us a infinite loop

#qs1
i = 1
while i <= 100:
    print(i)
    i += 1

#qs2
i = 100
while i >= 1:
    print(i)
    i -= 1

#qs3
i = 1
while i <= 10:
    print(3*i)
    i += 1

 #qs3
n = int(input("enter number: "))
i = 1
while i <= 10:
    print(n*i)
    i += 1

  #qs4
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

 #qs4
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0
while i < len(nums):
    print(nums[i])
    i += 1

#qs4
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx", i)
    i += 1   

#qs4
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx", i)
    else:
        print("finding..")
    i += 1              