#Rounding- the around() function increments the preceding digit or decimal point nearest to 1: if n>5 = 1, or or n<5 = 0
#
import numpy as np
sharad = np.around([-3.875, 3.875])
print(sharad)

#Floor()- round off decimals to the lower integer.

import numpy as np
sharad = np.floor([-3.875, 3.875])
print(sharad)

# ceil()- Rounding off decimal to the upper integer.

import numpy as np
sharad = np.ceil([-3.875, 3.875])
print(sharad)

#Summation: difference: addition is done between 2 argument
# whereas summation happens over an element,

# adding the  2 array .

import numpy as np
sharad1 = np.array([1,2,3])
sharad2 = np.array([1,2,3])
sharadnew = np.add([sharad1, sharad2])
print(sharadnew)

#sum the value in 2 array.

import numpy as np
sharad1 = np.array([1,2,3])
sharad2 = np.array([1,2,3])
sharadnew = np.sum([sharad1, sharad2])
print(sharadnew)

#Summation over an axis- if you specify axis=1, NumPy will sum the numbers in each array.

import numpy as np
sharad1 = np.array([1,2,3])
sharad2 = np.array([1,2,3])
sharadnew = np.sum([sharad1, sharad2], axis = 1)
print(sharadnew)

#cummulative sum:  means partially adding the element in array

# example: [1,2,3,4] would be[1, 1+2, 1+2+3, 1+2+3+4] = [1,3,6,10] represented by cumsum()

import numpy as np
sharad = np.array([1,2,3])
sharadnew = np.cumsum(sharad)
print(sharadnew)


