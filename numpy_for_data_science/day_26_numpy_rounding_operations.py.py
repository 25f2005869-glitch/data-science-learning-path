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

#quotient and mod(remainder)
#The divmod() function returns both the quotient and mod.

import numpy as np
sharad1 = np.array([10,11,12,13,14,15])
sharad2 = np.array([3,4,5,6,7,8,9,45])
sharadnew = divmod(sharad1, sharad2)
print(sharadnew)

#absolute() and abs() - do the same operation, but here we should use absolute() to avoid confusion with Python inbuilt function math.abs()

import numpy as np
sharad = np.array([-1,-2,-3,-4,-5])
sharadnew = np.absolute(sharad)
print(sharadnew)

#rounding decimal- there are 5 ways of rounding off the decimal in NumPy: truncation, fixed rounding, floor, ceil.

#truncation: trunc() and fix()

#Here we are truncation the following array,
#These commands remove the decimals and return the float numbers closest to zero.

import numpy as np
sharad = np.trunc([-3.875, 3.875])
print(sharad)

#fix()example

import numpy as np
sharad = np.fix([-3.875, 3.875])
print(sharad)

