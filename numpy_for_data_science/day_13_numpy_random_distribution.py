#you can also generate random numbers from an array choice()

from numpy import random
sharad = random.randint(100, size=(3,5))
print(sharad)

#you can also generate random numbers from an array choice()

from numpy import random
sharad = random.choice([3,5,7,9,1,4,6])
print(sharad)

#you can also generate random numbers from 2-D array choice()

from numpy import random
sharad = random.choice([3,5,7,9,1,4,6], size=(3,5))
print(sharad)

#numpy data distribution

#Data distribution is a list of all possible values and how often each value occurs.
#
# Such lists are important when working with statistics and data science,
#
# random distribution : probability function.

#Now, we will generate 1-D with 100 values where each value has to be 3, 5, 7, 9.
# The probability for the value 3 is set to be 0.1.
# The probability for the value 5 is set to be 0.3.
# The probability for the value 7 is set to be 0.6.
# The probability for the value 9 is set to be 0.

#The sum of all probability numbers should be '1'.

from numpy import random
sharad = random.choice([3,5,7,9,1,4,6],p=[0.1,0.3,0.6,0], size=(100))
print(sharad)

#now we will return 2-D with 3-D row containing 5 values:

from numpy import random
sharad = random.choice([3,5,7,9,1,4,6],p=[0.1,0.3,0.6,0], size=(3,5))
print(sharad)
