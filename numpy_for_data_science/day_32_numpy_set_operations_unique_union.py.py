#What is set?

#A set is a collection of unique elements.

#For creating the set:

#we can use NumPy's unique() method to find the unique elements for an array.:
                 
#Here we will convert the array with repeated elements to set.

import numpy as np
sharad = np.array([1,1,1,2,3,4,55,6,7])
sharadnew = np.unique(sharad)
Print(sharadnew)

#To find the unique value of  2 1D array, we will use unionld() method

import numpy as np
sharad1 = np.array([1,2,3,4])
sharad2 = np.array([3,4,5,6])
sharadnew = np.unionld(sharad1, sharad2)
Print(sharadnew)

#To find the only values that are present in both arrays,

#we will use intersectld() method.

import numpy as np
sharad1 = np.array([1,2,3,4])
sharad2 = np.array([3,4,5,6])
sharadnew = np.unionld(sharad1, sharad2, assume_unique= True)
Print(sharadnew)

#To find the only values that are in 1st set and not present in the 2nd set:

#use setfdiffld().

import numpy as np
sharad1 = np.array([1,2,3,4])
sharad2 = np.array([3,4,5,6])
sharadnew = np.unionld(sharad1, sharad2, assume_unique= True)
Print(sharadnew)

#To find the only values that are  not present in Both the sets

#use setxorld() method. :

import numpy as np
sharad1 = np.array([1,2,3,4])
sharad2 = np.array([3,4,5,6])
sharadnew = np.unionld(sharad1, sharad2, assume_unique= True)
Print(sharadnew)




