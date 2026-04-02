#create a filter array that will return only even elements from the original array.

import numpy as np
sharad = np.array([41,42,43,44])
sharadempty = []
for i in sharad:
    if i%2 == 0:
        sharadempty.append(True)
    else:
        sharadempty.append(False)
sharadnew = sharad[sharadempty]
print(sharadnew)

#yes , you can also create filter directly from array that will return only values higher than 42

import numpy as np
sharad = np.array([41,42,43,44])
emptysharad = sharad > 42
sharadnew = sharad[emptysharad]
print(emptysharad)
print(sharadnew)

#numpy random number

#Random meaning - something that cannot be predicted logically.

#Now we will generate float() via rand() from 0 to 1

from numpy import random
sharad = random.randint(100)
print(sharad)

#you can also generate float() via rand() from 0 to 1

from numpy import random
sharad = random.rand()
print(sharad)

#you can also generate random array

#we will generate a 1-D array containing 5 random int from 0 to 1

from numpy import random
sharad = random.randint(100, size=(5))
print(sharad)

#you can also generate random array

#we will generate a 2-D array  with 3 rows , each row containing 5 random int from 0 to 1

from numpy import random
sharad = random.randint(100, size=(3,5))
print(sharad)















