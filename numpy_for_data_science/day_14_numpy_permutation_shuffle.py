#Permutation refers to an arrangement of elements like [3, 2, 1] is permutation of [1, 2, 3] and vice versa.
#
# The NumPy random module provides two methods, shuffle() and permutation().
#
# Now we will randomly shuffle elements for the below array:

from numpy import random
import numpy as np
sharad = np.array([1,2,3,4,5])
random.shuffle(sharad)
print(sharad)

#Shuffle() method may change to the original array.
#
# Now we will randomly shuffle element for the below array.

from numpy import random
import numpy as np
sharad = np.array([1,2,3,4,5])
random.shuffle(sharad)
print(sharad)

# Now we will generate a permutation of element for the below array.(wrong method)

from numpy import random
import numpy as np
sharad = np.array([1,2,3,4,5])
random.permutation(sharad)
print(sharad)

# Now we will generate a permutation of element for the below array.

from numpy import random
import numpy as np
sharad = np.array([1,2,3,4,5])
random.permutation(sharad)
print(random.permutation(sharad))

#the permutation method leave the original array unchanged.

from numpy import random
import numpy as np
sharad = np.array([7,9,23,87])
random.permutation(sharad)
print(random.permutation(sharad))
