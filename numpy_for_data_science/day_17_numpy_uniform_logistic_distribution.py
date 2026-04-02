#Uniform distribution -  it is only made for probability(p)

#param -  a (lower bound-0.0), b (upper bound 1.0) size.

from numPy import random
sharad = random.uniform(size=(2, 3)
print (sharad)

#Visualize the generation of uniform distribution.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.uniform( size=1000),hist=False)
plt.show()

#Logistic distribution -  describe growth. It is basically important in aggregation and neural network.

#param - loc(mean- 0), scale(standard deviation, 1) , size

#Draw 2*2 sample of logistic with mean at 1 and standard deviation 2.

from numpy import random
sharad = random.logistic(loc=1,scale=2, size=(2,3))
print(sharad)

#Visualize the generation of logistic distribution.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.logistic( size=1000),hist=False)
plt.show()
