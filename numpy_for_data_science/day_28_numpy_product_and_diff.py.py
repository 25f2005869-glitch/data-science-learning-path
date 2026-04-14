#Products: use prod() function.

# Here we will find the product of the element of the below array.

import numpy as np
sharad = np.array([1,2,3,4])#1*2*3*4 = 24
sharadnew = np.prod(sharad)
print(sharadnew)

#Here we will find the product of element in 2 different array.

import numpy as np
sharad = np.array([1,2,3,4])
sharad2 = np.array([5,6,7,8])
sharadnew = np.prod([sharad1, sharad2])#1*2*3*4*5*6*7*8= 40320
print(sharadnew)

#product over an axis

import numpy as np
sharad = np.array([1,2,3,4])
sharad2 = np.array([5,6,7,8])
sharadnew = np.prod([sharad1, sharad], axis=1)
print(sharadnew)

##cummulative product:
#example the partial product of [1,2,3,4] is [1,1*2,1*2*3,1*2*3*4] = [1,2,6,24] represented by cumprod().

import numpy as np
sharad = np.array([5,6,7,8])
sharadnew = np.cumprod(sharad)
print(sharadnew)

#DIFFERENCE

#Difference used  diff() function for finding the difference

#example: [1,2,3,4], the discrete difference of this would be[2-1,3-2,4-3] = [1,1,1] by using diff().

import numpy as np
sharad = np.array([10,15,25,5])
#[5,10, -20] because 15-10=5,20-15=5, 5-25=-20
sharadnew = np.diff(sharad)
print(sharadnew)







