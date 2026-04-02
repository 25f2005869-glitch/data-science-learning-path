#Multinomial distribution - it is a generalization of binomial distribution,

#parameter - n(number of possibility or outcome),  pvals(list of possibility or outcome), size(shape of return array),

#draw outer sample for dice roll.

from numpy import random
sharad = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(sharad)

#Multinomial sample will not produce a single value, they will produce one value for each pvals.

#numpyexopnential distribution

#Exponential distribution, it is used for describing the time till next event that is like failure or success.

#param - scale (inverse of rate(see lam pisson dist.)),size

#Here we will draw a sample for exponential distribution with 2.0, scale, and 2* 3 size.

from numpy import random
sharad = random.exponential(scale=2, size=(2,3))
print(sharad)

#Visualization of exponential distribution.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.exponential( size=1000),hist=False)
plt.show()
