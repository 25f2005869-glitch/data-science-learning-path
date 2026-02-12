#qs1

age = int(input('enter your age:'))
if age > 18:
    print("eligible for voting card")

    #qs2

age = int(input('enter your age:'))
f = open("data.txt",'w')
f.write(age)
f.close

#qs3

f = open("data.txt",'r')
print(f.read())
f.close

#qs4

#f = open(filename,mode = 'r', buffering,encoding = None,error = None, newline = None,closedfd = True)
f = open('hello.txt')
if f:
    print("file successfully opened")

    #qs5

f = open('hello.txt','w')
if f:
    print("file successfully opened")
print(type(f))

#qs6

f = open('hello.txt','r')
if f:
    print("file successfully opened")
print(type(f))

#qs7

#f = open('hello.txt',mode = 'r',buffering = 10',encoding = 'utf-8')
if f:
    print("opened")
print(f)

#qs8

#f = open('hello.txt',mode = 'r',buffering = 10')
if f:
    print("opened")
print(f)

#qs9

#f = open('hello.txt','r', 'utf-8')
if f:
    print("opened")
print(f)

#qs10

f = open('hello.txt','r')
#operations
f.close()
