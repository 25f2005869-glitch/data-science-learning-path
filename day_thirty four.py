#ex-01
f=open("leetcode.txt",mode='r')

#operations

f.close()

print("rest of code")

#Error
#ex-01
f=open("leet-code.txt",mode='r')

#operations

f.close()

print("rest of code")

#ex-01
try:
   f=open("leetcode.txt",mode='r')
except Exception as obj:
   print(obj)

#operations

f.close()

print("rest of code")

#ex-01
try:
   f=open("leetcode.txt",mode='r')
   f.write("hello world)")
except Exception as obj:
   print(obj)
else:
   f.close()

print("rest of code")

#import #mysql.connector
#try:
   #mysql.connector.connect(
      #user='root',
      #password='shantanu@123'
      #host='localhost',
      #port=3306,
      #database='student'
   #)
#except:
    #print("cannot connect")

import sys
def format_traceback(exc_type,exc_value,exc_traceback):
   print("something went wrong")
   print(exc_type)
   print(exc_value)
   print(list(exc_traceback))

sys.excepthook=format_traceback
def display():
   print(1+"hello")

display()

from threading import *
from time import sleep
def display():
   for i in range(4):
      sleep(2)
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
   


   



