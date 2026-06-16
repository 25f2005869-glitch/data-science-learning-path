 #Ufunc - Transfer universal functions, they are a kind of function that operate on the array object

 #Ufunc-  also take additional arguments like where dtype and out,

 #vectorization -  converting the iterative statement into a vector-based statement

 #example without ufunc Here we will use Python build zip().

x = [1,2,3,4]
y = [4,5,6,7]
z = []
for i, j in zip(x=y):
     z.append(i+j)
print(z)

# with ufunc we will now use add() function

import numpy as np
x = [1,2,3,4]
y = [4,5,6,7]
z = np.add(x,y)
print(z)

#numpy create ufunc

#To create your own, ufunc you have to define a function

 #like you do a normal function in Python.

#Then you add it to the NumPy function with frompyfunc() method,

 #argument of frompyfunc() :function, input, output

 #creates your own ufunc  for addition.

import numpy as np
def myadd(x, y):
    return x+y

myadd = np.frompy(myadd, 2, 1)
print(myadd([1,2,3,4], [5,6,7,8]))


