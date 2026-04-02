#difference between numpy array copy and view.

# we will make a copy , change in original array, and display both.

import numpy as np
sharad = np.array([1, 2, 3, 4, 5])
sharad1 = sharad.copy()
print(sharad)
print(sharad1)

import numpy as np
sharad = np.array([1, 2, 3, 4, 5])
sharad1 = sharad.copy()
sharad[0] = 12
print(sharad)
print(sharad1)

#now we will make a view , change original, display both

import numpy as np
sharad = np.array([1, 2, 3, 4, 5])
sharad1 = sharad.view()
sharad[0] = 42
print(sharad)
print(sharad1)

# Lecture 7

#numpyarrayshape

#shape of an array - the shape of an array is the number of elements in each dimension

#Now we will try to get the shape of an array.

import numpy as np
sharad = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(sharad.shape)

#(2, 4) which the array has 2 dimension and its has 4 elements

#now we will create a 3-D array using ndmin:

import numpy as np
sharad = np.array([1,2,3,4], ndmin=5)
print(sharad)
print('shape of array is ', sharad.shape)





