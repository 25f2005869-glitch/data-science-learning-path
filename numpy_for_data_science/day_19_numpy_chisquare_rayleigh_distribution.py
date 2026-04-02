#Chi-square distribution, it is basically used as a basis to verify the hypothesis

 #param - DF (degree of freedom),

#size sample for square distribution with DF 2 with size 2 * 3.

from numpy import random
sharad = random.chisquare(df=2, size=(2,3))
print(sharad)

#Visualisation of square.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df =1, size=1000),hist=False)
plt.show()

#Rayleigh distribution

 #Rayleigh distribution -  it is used in single processing,

 #param - scale (standard deviation),

# how flat the distribution is, default (1.0) size,

# sample call r1 with scale of 20 with size of 2* 3.

from numpy import random
sharad = random.rayleigh(scale=2, size=(2,3))
print(sharad)

#Visualization of  Rayleigh distribution.the distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df =1, size=1000),hist=False)
plt.show()