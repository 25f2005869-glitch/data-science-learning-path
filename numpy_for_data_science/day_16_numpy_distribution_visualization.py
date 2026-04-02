#Poisson distribution  - could estimate how many time an event can happen.

#param - lam (number of occurrence or rate), size,

#generate a random 1* 10 distribution for the occurrence 2
#
from numpy import random
sharad = random.poisson(lam=2, size=10)
print(sharad)

#visualization of binomial distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.poisson(lam=2, size=1000),kde=False)
plt.show()

#.Present in both the plot is same figure normal and Poisson distribution.

from numpy import random
import matplotlib.pyplot as plt

import seaborn as sns
sns.distplot(random.normal(loc=50, scale=7, size=1000),
hist=False, label='Normal')
sns.distplot(random.poisson(lam=50,  size=1000),
hist=False, label='poisson')

plt.show()

#n*p = lam

#matplotlib(pyplot) - seaborn

#seaborn is a library that uses matplotlib underneath to plot graph i.r pyplot

##Distplot - distribution plot(curve plot - histogram)

import matplotlib.pyplot as plt
import seaborn as sns
sns distplot([0,1,2,3,4,5])
pli.show()

#plotting a distplot without the histogram

import matplotlib.pyplot as plt
import seaborn as sns
sns distplot([0,1,2,3,4,5], hist=False)
pli.show()



