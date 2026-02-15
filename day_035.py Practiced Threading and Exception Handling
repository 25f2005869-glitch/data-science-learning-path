from threading import *
from time import sleep
def display():
   for i in range(4):
      sleep(0.1)
      print("hello:"+10)

def show():
   for i in range(4):
      print("hello")
      sleep(0.5)

t1=Thread(target=display)
t2=Thread(target=show)
t1.start()
t2.start()
t1.join()
t2.join()
for i in range(4):
   print("Bye")

import threading 
from time import sleep
def custom_hook(args):
   print("Ecxeption occured in thread")
   print(args[0])
   print(args[1])
   print(args[2])
   print(args[3])
def display():
   for i in range(4):
      sleep(2)
      print("hello:"+10)

def show():
   for i in range(4):
      print("hello")
      sleep(0.5)

threading.excepthook=custom_hook
t1= threading.Thread(target=display)
t2=threading.Thread(target=show)
t1.start()
t2.start()
t1.join()
t2.join()
for i in range(4):
   print("Bye")

def get_square():
   try:
      num=int(input("Enter the number: "))
      print("square is:",num**2)
   except Exception as e:
        print(e)
        get_square()

get_square()

print("rest of code")

try:
   f = open('data.txt',mode='r')
   my_data = f.read()
   print(my_data)
except Exception as e:
   print(e)
else:
   print("read operation")
finally:
   f.close()

try:
   f = open('data.txt',mode='r')
   my_data = f.read()
   print(my_data)
except Exception as e:
   print(e)
else:
   print("read operation")
finally:
   try:
      f.close()
   except:
      pass
   
print("rest of code")

