 #paretoDistribution:, 80-20 ratio, (20% factors cause 80% outcome result)

 #param - , a (shape param),  size,

 #sample, for pareto distribution with shape 2 with size 2*3,

from numpy import random
sharad = random.pareto(a=2, size=(2,3))
print(sharad)

 #Visualization of distribution.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.pareto(a =1, size=1000),kde=False)
plt.show()

#Zipfdist

#Zipf Distribution -  it('s definition is like common word in English has occurred '

#nearly one/five times as of the most Hindi words. '

 # param -  a (dist param),  size,

 #sample for zipf  distribution with a as 2 with size 2 * 3.

from numpy import random
sharad = random.zipf(a=2, size=(2,3))
print(sharad)

 #Visualization of distribution.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sharad = random.zipf(a=2, size=1000)
sns.distplot(sharad,kde=False)
plt.show()