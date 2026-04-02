#Data types in python: string, integer, float, boolean,complex
#data type in numpy
#i for integer
#b for boolean
#u for unsigned integer
#f for float
#c for complex float
#m for timedelta
#M for datatime
#O for object
#S for string
#U for unicode string
#V - Memory

#checking the data type of numpy array -dtype

import numpy as np
sharad = np.array([1, 2, 3, 4])
print(sharad.dtype)

#checking the data type of numpy array - string

import numpy as np
sharad = np.array(['apple', 'banana', 'cherry'])
print(sharad.dtype)

#creating array with a defined data type:

import numpy as np
sharad = np.array([1, 2, 3, 4], dtype='5')
print(sharad)
print(sharad.dtype)

#now we will create an array with data type of 4 byte int:

import numpy as np
sharad = np.array([1, 2, 3, 4], dtype='i4')
print(sharad)
print(sharad.dtype)

#if a type is give in which the elements cannot be cast then nupy will raise error .
#what if a value cannot be converted?

import numpy as np
sharad = np.array([1.1, 2.1, 3.1])
print(sharad.dtype)

#converting data type in existing array - astype()

import numpy as np
sharad = np.array([1.1, 2.1, 3.1])
sharad1 = sharad.astype('i')
print(sharad1)
print(sharad.dtype)

#converting data type from integer to boolean

import numpy as np
sharad = np.array([1, 0, 3])
sharad1 = sharad.astype(bool)
print(sharad1)
print(sharad.dtype)
