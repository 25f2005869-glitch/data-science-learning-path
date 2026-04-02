#sort() - the numpy ndarray object has a function which is called sort(), and this will sort a specified array.

import numpy as np
sharad = np.array([3,2,1,0])
print(np.sort(sharad))

#sort the array alphabetically

import numpy as np
sharad = np.array(['banana','cherry','apple'])
print(np.sort(sharad))

#sort the boolean array:

import numpy as np
sharad = np.array([True,False,True])
print(np.sort(sharad))

#sorting the 2-D array

import numpy as np
sharad = np.array([[3,2,4], [5,0,1]])
print(np.sort(sharad))

#numpy filter array

#getting some elements out of an existing array and creating a new array is called filtering.

#A boolean index list is a list of boolean corresponding to indexes in the array.

#create an array from the element on index 0 to 2:

import numpy as np
sharad = np.array([41,42,43,44])
sharad1 = np.array([True,False,True,False])
finalsharad = sharad[sharad1]
print(finalsharad)

#now we will create a filter array

#that will return only values higher than 42

import numpy as np
sharad = np.array([41,42,43,44])
emptysharad = []
for element in sharad:
    if element > 42:
        emptysharad.append(True)
    else:
        emptysharad.append(False)
sharadnew = sharad[emptysharad]
print(emptysharad)
print(sharadnew)

