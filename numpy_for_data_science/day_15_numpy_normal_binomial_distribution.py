#Normal (Gaussian) distribution -  very important

#random.normal method- loc (mean), scale (standard deviation), size.

#We are generating a normal random normal distribution of size 2 * 3.

from numpy import random
sharad = random.normal(size=(2,3))
print(sharad)

#Here we will generate a random normal test of size 2 * 3 with mean at 1 and standard deviation at 2.

from numpy import random
sharad = random.normal(loc=1, scale=2, size=(2,3))
print(sharad)

#binomial dist-  discrete dist -  binary output,

#param- n (number of trials), p (probabilities), size (shape, return array)

# given 10 trials for a coin, which will generate 10 data points.

from numpy import random
sharad = random.binominal(n=10, p=0.5, size=10)
print(sharad)

#visualization of binomial distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=10, p=0.5, size=1000),
hist=True, kde=False)
plt.show()

#The difference between normal and binomial - normal (continuous) and binomial (discrete).
#
# i use 500 data points for binomial and 100 data points for normal distribution.

from numpy import random
import matplotlib.pyplot as plt

import seaborn as sns
sns.distplot(random.normal(loc=50, scale=5, size=1000),
hist=False, label='Normal')
sns.distplot(random.binomial(n=10, p=0.5, size=1000),
hist=False, label='Binominal')
plt.show()

