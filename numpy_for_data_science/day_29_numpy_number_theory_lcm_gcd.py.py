#Finding LCM lowest common multiple,

#here we will find the LCM of number

import numpy as np
sharad1 = 4
sharad2 = 6
sharadnew = np.lcm(sharad1 ,sharad2)
print(sharadnew)

#the answer of the above is 12 because LCM is both numbers(4*3=12 and 6*2=12)

#Finding the LCM in array:,

import numpy as np
sharad = np.array([3,6,9])
#the reduced() method is used the ufnuc, in this case the lcm() function on
#each element and it will reduce the array bt 1 dimension.
sharadnew = np.lcm.reduced(sharad)
print(sharadnew)

#Here we will find the sum of all of an array where the array contains all integers from 1 to 10.

import numpy as np
sharad = np.arrange(1,11)
sharadnew = np.lcm.reduced(sharad)
print(sharadnew)

#GCD

#Finding GCD, (greatest common denominator), also known as HCF, (highest common factor),

# here we will find the HCF of the below  2 numbers.

import numpy as np
sharad1 = 6
sharad2 = 9
sharadnew = np.gcd(sharad1 ,sharad2)
print(sharadnew)

#Answer will be 3 because that is the highest number

#and both can divide  by(6/3=2, 9/3=3)

#finding the GCD in an array,

#the reduced() method will be used the  ufunc, in this case the

#GCD() function on each element and it will reduce the array by 1 dimension.

import numpy as np
sharad = np.array([20,8,32,16,36])
sharadnew = np.gcd.reduced(sharad)
print(sharadnew)

#It will return 4 because 4 is the highest number of all values that can divide in between array.
