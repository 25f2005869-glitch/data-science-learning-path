#arithemetic operators: +, -, /, *

#by using ufunc additional like, where, dtype and out.

#here now we will use add()

import numpy as np
sharad1 = np.array([10,11,12,13,14,15])
sharad2 = np.array([20,21,22,23,24,25])
sharadnew = np.add(sharad1, sharad2)
print(sharadnew)

#example of substracting the value

import numpy as np
sharad1 = np.array([10,11,12,13,14,15])
sharad2 = np.array([20,21,22,23,24,25])
sharadnew = np.subtract(sharad1, sharad2)
print(sharadnew)

#example of multiplication

import numpy as np
sharad1 = np.array([10,11,12,13,14,15])
sharad2 = np.array([20,21,22,23,24,25])
sharadnew = np.multiply(sharad1, sharad2)
print(sharadnew)

##example of divide()

import numpy as np
sharad1 = np.array([10,11,12,13,14,15])
sharad2 = np.array([20,21,22,23,24,25])
sharadnew = np.divide(sharad1, sharad2)
print(sharadnew)

#power() function raises the value from the 1st rray to the power of the values of the 2nd array and return the results in a new array.

import numpy as np
sharad1 = np.array([10,11,12,13,14,15])
sharad2 = np.array([3,4,5,6,7,8,9,45])
sharadnew = np.power(sharad1, sharad2)
print(sharadnew)

# remainder - mod() and remainder() functions return the remainder of the 1st array corresponding to the 2nd array, and result in the new array

import numpy as np
sharad1 = np.array([10,11,12,13,14,15])
sharad2 = np.array([3,4,5,6,7,8,9,45])
sharadnew = np.mod(sharad1, sharad2)
print(sharadnew)

# by using remainder()

import numpy as np
sharad1 = np.array([10,11,12,13,14,15])
sharad2 = np.array([3,4,5,6,7,8,9,45])
sharadnew = np.remainder(sharad1, sharad2)
print(sharadnew)